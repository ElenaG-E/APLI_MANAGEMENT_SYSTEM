import mysql.connector
from mysql.connector import errorcode

def generar_conexion():
    config = {
        'host': 'localhost',
        'user': 'root',
        'password': '',
        'database': 'api_management_1'
    }
    try:
        conexion = mysql.connector.connect(**config)
        if conexion.is_connected():
            print("Conexión exitosa a la base de datos.")
            return conexion
        else:
            print("No fue posible conectarse a la base de datos.")
            return None
    except mysql.connector.Error as error:
        if error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Acceso denegado, usuario o contraseña incorrectos.")
        elif error.errno == errorcode.ER_BAD_DB_ERROR:
            print("Su base de datos NO existe.")
        else:
            print(f"Error: {error}")
        return None

# No cierres la conexión aquí, ya que quieres usarla más tarde.