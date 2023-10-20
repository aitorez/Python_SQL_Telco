import pandas as pd
import sqlite3
from conection_sql_lite import*

% run cdr_simulator.py 
# Ejemplo de DataFrame ------------------------------------------------------------------

datos = {'nombre': ['Alice', 'Bob', 'Charlie'],
         'edad': [30, 35, 25]}
df = pd.DataFrame(datos)


# Función principal para el menú de opciones -----------------------------------------------

def menu():
    conn = conectar_base_de_datos()
    
    while True:
        print("\nOpciones:")
        print("1. Crear una tabla nueva desde un DataFrame")
        print("2. Borrar una tabla")
        print("3. Salir\n")
        
        opcion = input("Elige una opción (1-3): ")
        
        if opcion == '1':
            # Cargar un DataFrame existente
            print("Ingresa el nombre del DataFrame existente:")
            nombre_df = input("Nombre del DataFrame: ")
            
            try:
                df = globals()[nombre_df]  # Obtener el DataFrame según el nombre ingresado
                nombre_tabla = input("Ingresa el nombre de la nueva tabla: ")
                crear_tabla_desde_dataframe(conn, df, nombre_tabla)
                
            except KeyError:
                print(f"No se encontró un DataFrame con el nombre '{nombre_df}'.")
                
        elif opcion == '2':borrar_tabla(conn)
            
        elif opcion == '3':
        
            conn.close()
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")


# EJECUCION -----------------------------------------------------------------------------------
menu()