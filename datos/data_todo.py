from modelos.todo import Todo  # Asegúrate de que este import sea correcto
from datos.conexion_db import generar_conexion

# Crear (Insertar)
def insertar_todos(id_todo=0, user_id=0, title='', completed=False):
    # Crear una instancia de la clase Todo
    nuevo_todo = Todo(id_todo, user_id, title, completed)
    
    conn = generar_conexion()
    cursor = conn.cursor()
    try:
        insertar_todos = """
            INSERT INTO todos(id_todo, user_id, title, completed) VALUES (%s, %s, %s, %s);
        """
        cursor.execute(insertar_todos, (nuevo_todo.id_todo, nuevo_todo.user_id, nuevo_todo.title, nuevo_todo.completed))
        conn.commit()  # Asegúrate de hacer commit después de la inserción
    except Exception as e:
        print(f"Ocurrió un error al insertar el todo: {e}")
    finally:
        cursor.close()
        conn.close()

# Leer (Seleccionar)
def obtener_todos():
    conn = generar_conexion()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM todos;")
        return cursor.fetchall()
    except Exception as e:
        print(f"Ocurrió un error al obtener los todos: {e}")
        return []
    finally:
        cursor.close()
        conn.close()

# Actualizar
def actualizar_todos(id_todo=0, user_id=0, title='', completed=False):
    conn = generar_conexion()
    cursor = conn.cursor()
    try:
        actualizar_todos = """
            UPDATE todos SET user_id = %s, title = %s, completed = %s WHERE id_todo = %s;
        """
        cursor.execute(actualizar_todos, (user_id, title, completed, id_todo))
        conn.commit()  # Asegúrate de hacer commit después de la actualización
    except Exception as e:
        print(f"Ocurrió un error al actualizar el todo: {e}")
    finally:
        cursor.close()
        conn.close()

# Eliminar
def eliminar_todos(id_todo=0):
    conn = generar_conexion()
    cursor = conn.cursor()
    try:
        eliminar_todos = """
            DELETE FROM todos WHERE id_todo = %s;
        """
        cursor.execute(eliminar_todos, (id_todo,))
        conn.commit()  # Asegúrate de hacer commit después de la eliminación
    except Exception as e:
        print(f"Ocurrió un error al eliminar el todo: {e}")
    finally:
        cursor.close()
        conn.close()