import random
import pandas as pd
from datetime import datetime, timedelta
from functions import*

pais = pd.read_csv(r'/Users/aitorelordizamora/Documents/GitHub/telco/Notebook/Proyecto_ICOX_FIJA/reference paises iso/paises.csv', sep=',')
pais = pais[pais['phone_code'].notnull()]

# Genera un número de teléfono MOC con prefijo español y 9 dígitos adicionales
def generar_numero_moc_origen():
    
    prefijo_espanol = "+34"  # Prefijo español
    nueve_digitos = "".join([str(random.randint(0, 9)) for _ in range(9)])
    return f"{prefijo_espanol}{nueve_digitos}"

def generar_numero_moc_destino():
    return f"+{random.randint(1, 99)}{random.randint(100, 999)}{random.randint(1000, 9999)}"
    
# Genera un número de teléfono aleatorio para MTC
def generar_numero_mtc():
    prefijo_espanol = "+34"
    probabilidad_numeros_especiales = 0.25  # 25% de probabilidad de número especial
    if random.random() < probabilidad_numeros_especiales:
        numeros_especiales = ["1002","1003","1004","100", "123", "911", "0800", "555", "666", "777", "888", "999", "112", "113", "114", "115", "116", "117", "118", "119", "900", "901", "902", "903", "904", "905", "906", "907", "908", "909"]
        return random.choice(numeros_especiales)
    
    else:
        nueve_digitos = "".join([str(random.randint(0, 9)) for _ in range(9)])
        return f"{prefijo_espanol}{nueve_digitos}"
    
    
    

# Genera una duración de llamada aleatoria en segundos
def generar_duracion_llamada():
    return random.randint(1, 3600)  # Duración entre 1 segundo y 1 hora

# Genera una fecha y hora aleatoria en los últimos 30 días
def generar_fecha_hora():
    fecha_inicio = datetime(2023, 1, 1)
    fecha_fin = datetime(2023, 12, 31)
    # Genera una fecha aleatoria dentro del rango de 2023
    fecha_hora = fecha_inicio + timedelta(days=random.randint(0, (fecha_fin - fecha_inicio).days))
    # Genera una hora aleatoria en formato HH:MM:SS
    hora = f"{random.randint(0, 23):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    
    # Combina la fecha y la hora
    return f"{fecha_hora.strftime('%Y-%m-%d')} {hora}"

# Crea un registro de CDR realista
def crear_registro_cdr():
    if random.random() < 0.7:
        origen = generar_numero_moc_origen()
        destino = generar_numero_moc_destino()
        tipo = "MOC"  # Llamada emitida
    else:
        origen = generar_numero_moc_destino()
        destino = generar_numero_moc_origen()
        tipo = "MTC"  # Llamada recibida
    
    duracion = generar_duracion_llamada()
    fecha_hora = generar_fecha_hora()
    
    return {"Origen": origen, "Destino": destino, "Duracion": duracion, "Fecha_Hora": fecha_hora, "Sentido": tipo}

# Genera un DataFrame con registros simulados de CDR
def generar_dataframe_cdrs(cantidad):
    cdrs = []
    
    for _ in range(cantidad):
        cdr = crear_registro_cdr()
        
        # Ajusta el número de llamadas durante el fin de semana (25% menos)
        dia_semana = datetime.strptime(cdr["Fecha_Hora"], "%Y-%m-%d %H:%M:%S").weekday()
        if dia_semana >= 5:  # Día de la semana 5 es sábado, 6 es domingo
            if random.random() < 0.25:  # 25% de probabilidad de omitir la llamada
                continue
        
        cdrs.append(cdr)
    
    return pd.DataFrame(cdrs)

# Ejemplo de generación de un DataFrame de CDRs
cantidad_registros = 50000
df_cdrs_i = generar_dataframe_cdrs(cantidad_registros)
df_cdrs_i['Minutos'] = (df_cdrs_i['Duracion']/60).round(2)

# Limpiar el signo "+" de las columnas "Telefono1" y "Telefono2"
df_cdrs_i["Origen_corregido"] = df_cdrs_i["Origen"].str.replace("+", "")
df_cdrs_i["Destino_corregido"] = df_cdrs_i["Destino"].str.replace("+", "")
df_cdrs_i['Tipo evento'] = 'Internacional'

df_cdrs_i['Max_coincidencia'] = df_cdrs_i['Destino_corregido'].apply(lambda x: encontrar_maxima_coincidencia(x, pais['phone_code']))
df_cdrs_i = df_cdrs_i.merge(pais, how='left', left_on='Max_coincidencia', right_on = 'phone_code')
print(df_cdrs_i.columns)