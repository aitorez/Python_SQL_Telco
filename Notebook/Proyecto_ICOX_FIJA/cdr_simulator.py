import random
import pandas as pd
from datetime import datetime, timedelta

# Genera un número de teléfono MOC con prefijo español y 9 dígitos adicionales
def generar_numero_moc():
    
    prefijo_espanol = "+34"  # Prefijo español
    
    probabilidad_numeros_especiales = 0.25  # 25% de probabilidad de número especial
    if random.random() < probabilidad_numeros_especiales:
        numeros_especiales = ["1002","1003","1004","100", "123", "911", "0800", "555", "666", "777", "888", "999", "112", "113", "114", "115", "116", "117", "118", "119", "900", "901", "902", "903", "904", "905", "906", "907", "908", "909"]
        return random.choice(numeros_especiales)
    else:
        nueve_digitos = "".join([str(random.randint(0, 9)) for _ in range(9)])
        return f"{prefijo_espanol}{nueve_digitos}"


# Genera un número de teléfono aleatorio para MTC
def generar_numero_mtc():
    return f"+{random.randint(1, 99)}{random.randint(100, 999)}{random.randint(1000, 9999)}"

# Genera una duración de llamada aleatoria en segundos
def generar_duracion_llamada():
    return random.randint(1, 3600)  # Duración entre 1 segundo y 1 hora

# Genera una fecha y hora aleatoria en los últimos 30 días
def generar_fecha_hora():
    ahora = datetime.now()
    fecha_hora = ahora - timedelta(days=random.randint(1, 30))
    return fecha_hora.strftime("%Y-%m-%d %H:%M:%S")

# Crea un registro de CDR realista
def crear_registro_cdr():
    if random.random() < 0.6:
        origen = generar_numero_moc()
        destino = generar_numero_mtc()
        tipo = "MOC"  # Llamada emitida
    else:
        origen = generar_numero_mtc()
        destino = generar_numero_moc()
        tipo = "MTC"  # Llamada recibida
    
    duracion = generar_duracion_llamada()
    fecha_hora = generar_fecha_hora()
    
    return {"Origen": origen, "Destino": destino, "Duracion": duracion, "Fecha_Hora": fecha_hora, "Tipo": tipo}

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
cantidad_registros = 5000
df_cdrs = generar_dataframe_cdrs(cantidad_registros)
df_cdrs['Minutos'] = (df_cdrs['Duracion']/60).round(2)
# Limpiar el signo "+" de las columnas "Telefono1" y "Telefono2"
df_cdrs["Origen_corregido"] = df_cdrs["Origen"].str.replace("+", "")
df_cdrs["Destino_corregido"] = df_cdrs["Destino"].str.replace("+", "")