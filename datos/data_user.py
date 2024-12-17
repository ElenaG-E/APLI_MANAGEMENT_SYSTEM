from modelos.users import User  # Asegúrate de que este import sea correcto
from datos.conexion_db import generar_conexion

# Crear (Insertar)
def insertar_usuario(name='', username='', email='', phone='', website=''):
    # Crear una instancia de la clase User
    nuevo_usuario = User(name, username, email, phone, website)
    
    conn = generar_conexion()
    cursor = conn.cursor()
    try:
        insertar_usuarios = """
            INSERT INTO users(name, username, email, phone, website) VALUES (%s, %s, %s, %s, %s);
        """
        cursor.execute(insertar_usuarios, (nuevo_usuario.name, nuevo_usuario.username, nuevo_usuario.email, nuevo_usuario.phone, nuevo_usuario.website))
        conn.commit()  # Asegúrate de hacer commit después de la inserción
    except Exception as e:
        print(f"Ocurrió un error al insertar el usuario: {e}")
    finally:
        cursor.close()
        conn.close()

# Leer (Seleccionar)
def obtener_usuarios():
    conn = generar_conexion()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM users;")
        return cursor.fetchall()
    except Exception as e:
        print(f"Ocurrió un error al obtener los usuarios: {e}")
        return []
    finally:
        cursor.close()
        conn.close()

# Actualizar
def actualizar_usuario(id_user, name, username, email, phone, website):
    conn = generar_conexion()
    cursor = conn.cursor()
    try:
        actualizar_usuarios = """
            UPDATE users SET name = %s, username = %s, email = %s, phone = %s, website = %s WHERE id_user = %s;
        """
        cursor.execute(actualizar_usuarios, (name, username, email, phone, website, id_user))
        conn.commit()  # Asegúrate de hacer commit después de la actualización
    except Exception as e:
        print(f"Ocurrió un error al actualizar el usuario: {e}")
    finally:
        cursor.close()
        conn.close()

# Eliminar
def eliminar_usuario(id_user):
    conn = generar_conexion()
    cursor = conn.cursor()
    try:
        eliminar_usuarios = """
            DELETE FROM users WHERE id_user = %s;
        """
        cursor.execute(eliminar_usuarios, (id_user,))
        conn.commit()  # Asegúrate de hacer commit después de la eliminación
    except Exception as e:
        print(f"Ocurrió un error al eliminar el usuario: {e}")
    finally:
        cursor.close()
        conn.close()