from modelos.addresses import Address  # Asegúrate de que este import sea correcto
from datos.conexion_db import generar_conexion

# Crear (Insertar)
def insertar_address(id_address=0, street='', suite='', city='', zipcode='', id_geo=0):
    # Crear una instancia de la clase Address
    nueva_direccion = Address(id_geo, id_address, street, suite, city, zipcode)
    
    conn = generar_conexion()
    cursor = conn.cursor()
    try:
        insertar_direcciones = """
            INSERT INTO addresses(id_address, street, suite, city, zipcode, id_geo) VALUES (%s, %s, %s, %s, %s, %s);
        """
        cursor.execute(insertar_direcciones, (nueva_direccion.id_address, nueva_direccion.street, nueva_direccion.suite, nueva_direccion.city, nueva_direccion.zipcode, nueva_direccion.id_geo))
        conn.commit()  # Asegúrate de hacer commit después de la inserción
    except Exception as e:
        print(f"Ocurrió un error al insertar la dirección: {e}")
    finally:
        cursor.close()
        conn.close()

# Leer (Seleccionar)
def obtener_direcciones():
    conn = generar_conexion()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM addresses;")
        return cursor.fetchall()
    except Exception as e:
        print(f"Ocurrió un error al obtener las direcciones: {e}")
        return []
    finally:
        cursor.close()
        conn.close()

# Actualizar
def actualizar_address(id_address=0, street='', suite='', city='', zipcode='', id_geo=0):
    conn = generar_conexion()
    cursor = conn.cursor()
    try:
        actualizar_direcciones = """
            UPDATE addresses SET street = %s, suite = %s, city = %s, zipcode = %s, id_geo = %s WHERE id_address = %s;
        """
        cursor.execute(actualizar_direcciones, (street, suite, city, zipcode, id_geo, id_address))
        conn.commit()  # Asegúrate de hacer commit después de la actualización
    except Exception as e:
        print(f"Ocurrió un error al actualizar la dirección: {e}")
    finally:
        cursor.close()
        conn.close()

# Eliminar
def eliminar_address(id_address=0):
    conn = generar_conexion()
    cursor = conn.cursor()
    try:
        eliminar_direcciones = """
            DELETE FROM addresses WHERE id_address = %s;
        """
        cursor.execute(eliminar_direcciones, (id_address,))
        conn.commit()  # Asegúrate de hacer commit después de la eliminación
    except Exception as e:
        print(f"Ocurrió un error al eliminar la dirección: {e}")
    finally:
        cursor.close()
        conn.close()