import servicios.ws_jsonplaceholder as ws_json
import mysql.connector
from mysql.connector import errorcode
from modelos.users import User

def procesar_datos_usuarios():
    usuarios_api = ws_json.obtener_usuarios_api()
    #usuarios_api = obtener_usuarios_api()
    #data_usuarios = json.loads(json.dumps(usuarios_api))
    usuarios = [User()]

    for usr in usuarios_api:
        nuevo_usuario = User()
        nuevo_usuario.id_user = usr['id']
        nuevo_usuario.name = usr['name']
        nuevo_usuario.username = usr['username']
        nuevo_usuario.email = usr['email']
        nuevo_usuario.phone = usr['phone']
        nuevo_usuario.website = usr['website']
        
        nuevo_usuario.street = usr['address']['street']
        nuevo_usuario.suite = usr['address']['suite']
        nuevo_usuario.city = usr['address']['city']
        nuevo_usuario.zipcode = usr['address']['zipcode']

        nuevo_usuario.lat = usr['address']['geo']['lat']
        nuevo_usuario.lng = usr['address']['geo']['lng']
        
        nuevo_usuario.company_name = usr['company']['name']
        nuevo_usuario.catchPhrase = usr['company']['catchPhrase']
        nuevo_usuario.bs = usr['company']['bs']

        usuarios.append(nuevo_usuario)



    
