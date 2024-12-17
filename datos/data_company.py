from modelos.companies import Company  # Asegúrate de que este import sea correcto
from datos.conexion_db import generar_conexion

# Crear (Insertar)
def insertar_company(id_company=0, company_name='', catchPhrase='', bs=''):
    # Crear una instancia de la clase Company
    nueva_compania = Company(id_company, company_name, catchPhrase, bs)
    
    conn = generar_conexion()
    cursor = conn.cursor()
    try:
        insertar_companias = """
            INSERT INTO companies(id_company, company_name, catchPhrase, bs) VALUES (%s, %s, %s, %s);
        """
        cursor.execute(insertar_companias, (nueva_compania.id_company, nueva_compania.company_name, nueva_compania.catchPhrase, nueva_compania.bs))
        conn.commit()  # Asegúrate de hacer commit después de la inserción
    except Exception as e:
        print(f"Ocurrió un error al insertar la compañía: {e}")
    finally:
        cursor.close()
        conn.close()

# Leer (Seleccionar)
def obtener_companias():
    conn = generar_conexion()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM companies;")
        return cursor.fetchall()
    except Exception as e:
        print(f"Ocurrió un error al obtener las compañías: {e}")
        return []
    finally:
        cursor.close()
        conn.close()

# Actualizar
def actualizar_company(id_company=0, company_name='', catchPhrase='', bs=''):
    conn = generar_conexion()
    cursor = conn.cursor()
    try:
        actualizar_companias = """
            UPDATE companies SET company_name = %s, catchPhrase = %s, bs = %s WHERE id_company = %s;
        """
        cursor.execute(actualizar_companias, (company_name, catchPhrase, bs, id_company))
        conn.commit()  # Asegúrate de hacer commit después de la actualización
    except Exception as e:
        print(f"Ocurrió un error al actualizar la compañía: {e}")
    finally:
        cursor.close()
        conn.close()

# Eliminar
def eliminar_company(id_company=0):
    conn = generar_conexion()
    cursor = conn.cursor()
    try:
        eliminar_companias = """
            DELETE FROM companies WHERE id_company = %s;
        """
        cursor.execute(eliminar_companias, (id_company,))
        conn.commit()  # Asegúrate de hacer commit después de la eliminación
    except Exception as e:
        print(f"Ocurrió un error al eliminar la compañía: {e}")
    finally:
        cursor.close()
        conn.close()