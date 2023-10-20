import pandas as pd
import sqlite3
from conection_sql_lite import*
import subprocess

from cdr_national_simulator import df_cdrs


# Ejemplo de DataFrame ------------------------------------------------------------------

#df_cdrs1



# Función principal para el menú de opciones -----------------------------------------------

# Función principal para el menú de opciones
def menu():
    conn = conectar_base_de_datos()
    
    while True:
        print("\n##################################################")
        print("\nOpciones:\n")
        print("1. Crear una tabla nueva desde un DataFrame")
        print("2. Borrar una tabla")
        print("3. Listar tablas en la base de datos")
        print("4. Mostrar información de una tabla")
        print("5. Salir\n")
        print("##################################################")
        
        opcion = input("Elige una opción (1-5): ")
        
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
                
        elif opcion == '2':
            print("\nRESPUESTA:\n")
            borrar_tabla(conn)
            
        elif opcion == '3':
            print("\nRESPUESTA:\n")
            listar_tablas(conn)
            
        elif opcion == '4':
            print("\nRESPUESTA:\n")
            mostrar_informacion_tabla(conn)
            
        elif opcion == '5':
            conn.close()
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

# EJECUCION -----------------------------------------------------------------------------------
menu()