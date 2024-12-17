import mysql.connector
from mysql.connector import errorcode
import requests
import datos.conexion_db as bd

from modelos.addresses import Address  # Asegúrate de que este import sea correcto
from datos.conexion_db import generar_conexion

from modelos.companies import Company  # Asegúrate de que este import sea correcto
from datos.conexion_db import generar_conexion

from modelos.geos import Geo

import negocios.encriptacion as encriptacion
import negocios.procesar_urls as urls 
import negocios.procesar_usuarios as usuarios
import servicios.servicio_todo as todo
import servicios.serper_test as serper_test 
import servicios.ws_jsonplaceholder as ws_jsonplaceholder

#encriptacion.encriptar("StringTest") 
#todo.consulta_api

bd.generar_conexion

from datos.data_user import insertar_usuario, obtener_usuarios, actualizar_usuario, eliminar_usuario

def main():
    # Insertar un nuevo usuario
    #insertar_usuario("Juan Pérez", "juanp", "juan@example.com", "123456789", "www.juanp.com")
    
    # Obtener y mostrar todos los usuarios
    #usuarios = obtener_usuarios()
    #print("Usuarios en la base de datos:")
    #for usuario in usuarios:
        #print(usuario)

    # Actualizar un usuario
    actualizar_usuario(1, "Juan Pérez", "juanp_updated_1", "juan_updated@example.com", "987654321", "www.juanp_updated.com")

    # Eliminar un usuario
    #eliminar_usuario(1)

if __name__ == "__main__":
    main()
from datos.data_todo import insertar_todos, obtener_todos, actualizar_todos, eliminar_todos

def main():
    insertar_todos(1, 'Comprar leche', 'True', 2)

def main():
    # Generar la conexión
    conexion = generar_conexion()
    
    if conexion:
        # Aquí puedes realizar operaciones con la base de datos
        cursor = conexion.cursor()
        
        # Ejemplo: Obtener datos de una tabla
        cursor.execute("SELECT * FROM users;")
        resultados = cursor.fetchall()
        
        for fila in resultados:
            print(fila)
        
        # Cerrar el cursor
        cursor.close()
        
        # Cerrar la conexión
        conexion.close()
        print("Conexión cerrada.")

if __name__ == "__main__":
    main()