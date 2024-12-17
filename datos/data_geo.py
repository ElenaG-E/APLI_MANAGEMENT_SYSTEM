from modelos.geos import Geo  # Asegúrate de que este import sea correcto
from datos.conexion_db import generar_conexion

# Crear (Insertar)
def insertar_geo(id_geo=0, lat='', lng=''):
    # Crear una instancia de la clase Geo
    nueva_geo = Geo(id_geo, lat, lng)
    
    conn = generar_conexion()
    cursor = conn.cursor()
    try:
        insertar_geos = """
            INSERT INTO geo(id_geo, lat, lng) VALUES (%s, %s, %s);
        """
        cursor.execute(insertar_geos, (nueva_geo.id_geo, nueva_geo.lat, nueva_geo.lng))
        conn.commit()  # Asegúrate de hacer commit después de la inserción
    except Exception as e:
        print(f"Ocurrió un error al insertar la geo: {e}")
    finally:
        cursor.close()
        conn.close()

# Leer (Seleccionar)
def obtener_geos():
    conn = generar_conexion()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM geo;")
        return cursor.fetchall()
    except Exception as e:
        print(f"Ocurrió un error al obtener las geos: {e}")
        return []
    finally:
        cursor.close()
        conn.close()

# Actualizar
def actualizar_geo(id_geo=0, lat='', lng=''):
    conn = generar_conexion()
    cursor = conn.cursor()
    try:
        actualizar_geos = """
            UPDATE geo SET lat = %s, lng = %s WHERE id_geo = %s;
        """
        cursor.execute(actualizar_geos, (lat, lng, id_geo))
        conn.commit()  # Asegúrate de hacer commit después de la actualización
    except Exception as e:
        print(f"Ocurrió un error al actualizar la geo: {e}")
    finally:
        cursor.close()
        conn.close()

# Eliminar
def eliminar_geo(id_geo=0):
    conn = generar_conexion()
    cursor = conn.cursor()
    try:
        eliminar_geos = """
            DELETE FROM geo WHERE id_geo = %s;
        """
        cursor.execute(eliminar_geos, (id_geo,))
        conn.commit()  # Asegúrate de hacer commit después de la eliminación
    except Exception as e:
        print(f"Ocurrió un error al eliminar la geo: {e}")
    finally:
        cursor.close()
        conn.close()