import sqlite3
import pandas as pd

# Función para conectar a la base de datos
def conectar_base_de_datos():
    return sqlite3.connect('proyecto_icox.db')

# Función para crear una tabla nueva desde un DataFrame
def crear_tabla_desde_dataframe(conn, dataframe, nombre_tabla):
    cursor = conn.cursor()
    
    # Obtener el nombre y tipo de datos de las columnas del DataFrame
    # Usaremos TEXT para todos los tipos de datos en este ejemplo
    columnas = ", ".join([f"{col} TEXT" for col in dataframe.columns])
    # Preguntar al usuario qué hacer si la tabla ya existe
    opcion = input(f"La tabla '{nombre_tabla}' ya existe. ¿Deseas reemplazarla ('r'), añadir datos ('a') o cancelar ('c')? ")
    
    if opcion.lower() == 'c':
        print("Operación cancelada.")
        return
    elif opcion.lower() == 'r':
        
        comando_sql = f'DROP TABLE IF EXISTS {nombre_tabla}'
        cursor.execute(comando_sql)
        print(f"La tabla '{nombre_tabla}' será reemplazada.")
        
    elif opcion.lower() == 'a':
        
        print(f"Se añadirán datos a la tabla '{nombre_tabla}'.")
        
    else:
        print("Opción no válida. Operación cancelada.")
        return
    
    # Crear la tabla y, si se eligió 'a', insertar datos del DataFrame
    comando_sql = f'CREATE TABLE {nombre_tabla} ({columnas})'
    cursor.execute(comando_sql)
    
    if opcion.lower() == 'a':
        
        dataframe.to_sql(nombre_tabla, conn, if_exists='append', index=False)
        
    else:
        
        dataframe.to_sql(nombre_tabla, conn, if_exists='replace', index=False)
    
    conn.commit()
    
    print(f'Se ha creado la tabla {nombre_tabla} y se han insertado los datos.')
  
    
# Función para borrar una tabla
def borrar_tabla(conn):
    nombre_tabla = input("Ingresa el nombre de la tabla a borrar: ")
    cursor = conn.cursor()
    
    try:
        comando_sql = f'DROP TABLE IF EXISTS {nombre_tabla}'
        cursor.execute(comando_sql)
        conn.commit()
        print(f'Se ha borrado la tabla {nombre_tabla}.')
        
    except sqlite3.Error as e:
        
        print(f'Error al borrar la tabla {nombre_tabla}: {str(e)}')

# Función para listar las tablas en la base de datos
def listar_tablas(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tablas = cursor.fetchall()
    print("Tablas en la base de datos:")
    for tabla in tablas:
        print(tabla[0])

# Función para mostrar información de una tabla
def mostrar_informacion_tabla(conn):
    nombre_tabla = input("Ingresa el nombre de la tabla: ")
    cursor = conn.cursor()
    cursor.execute(f"PRAGMA table_info({nombre_tabla});")
    columnas = cursor.fetchall()
    print(f"Información de la tabla '{nombre_tabla}':")
    for col in columnas:
        print(f"Nombre columna: {col[1]}, Tipo de dato: {col[2]}")