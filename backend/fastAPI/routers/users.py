# -*- coding: utf-8 -*-

from fastapi import APIRouter, HTTPException #con api router podemos crear rutas, y con el httpexce... podemos manejas los tipos de status que nos da el server y las excepciones o aviso que queremos que muestre
from pydantic import BaseModel #para definir una identidad

router = APIRouter(prefix="/users" ,
                   tags=["users"],
                   responses= {404 : {"message" : "no encontrado"}}) #indicamos que va a ser un router-- con el prefix como va a ser su ruta de acceso generica, con tags indicamos como va a aperecer en nuestra documentacion, y responses es el mensaje que va a mostrar en el caso de que falle el ingreso a esta ruta



#endidad user
class User(BaseModel): #BaseModel nos da la capacidad de crear una ideantidad
    id: int
    nombre :str
    apellido: str
    edad: int
    
    
#creamos una base de datos prototipo con los objetos utilizando la class user  para poder trabajar simulando una DataBase
users_list = [User(id = 1,nombre ="Franco", apellido="Argüello", edad=29),
              User(id = 2, nombre="Ivana", apellido="Aquino", edad=32),
              User(id = 3,nombre="Thiago", apellido="Argüello", edad=13)]


###############################################################################
#aca nos crea un json automaticamente, nos muestra nuestra base de Datos
@router.get("") 
async def users():
    return  users_list


###############################################################################
#hacer un get por path de url, lo usamos para parametros fijos que no pueden cambiar y obligatorios
@router.get("/{id}") #entre llaves ponemos el parametro que queremos captuar e interpretar 
async def users(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return  list(users)[0]
    except:
        raise HTTPException(status_code=404, detail= "No se ha encontrado el usuario" )
    


###############################################################################
#hacer un get por query    /?parametro=valor Usamos query cuando tenemos parametros que no sean fijos o puedan variar,

@router.get("/") #entre llaves ponemos el parametro que queremos captuar e interpretar 
                        #http://127.0.0.1:8000/user/?id=2
async def usersquery(id: int):
    return search_user(id)
    
    
    
#funcion para buscar un usuario por su Id    
def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return  list(users)[0]
    except:
        raise HTTPException(status_code=404, detail= "No se ha encontrado el usuario" )
    


#########################################################

@router.post("/", status_code= 201) #entre llaves ponemos el parametro que queremos captuar e interpretar 
async def user(user : User): #le pasamos como parametro un usuario de tipo Useer
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=404, detail= "El usuario ya existe" ) #cuando lanzamos un error tenemos que usar un raise no un return 
        
    else:
        users_list.append(user)
        return {"se agrego con exito el usuario"}
    
    
###########################################################
@router.put("/") #put usamos cuando vamos a actualizar el total de la info
async def user(user : User):
    found = False
    
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True #cambiamos el estado a True ya que hay coincidencia
            
    if not found: #con esto controlamos si se actualizo o no el usuario, invertimos el valor de found para forzar la condicion negativa
        raise HTTPException(status_code=404, detail= "El usuario no se encontro para modificarlo" )
    else:
        return user #con este else evitamos que nos aparezca un null como respuesta en el server y nos aparezca los datos para confirmar bien la modificacion y no solo el 200 ok con el null
    
#############################################################33
@router.delete("/{id}") # para borrar un usuario
async def user(id:int):
    found = False
    
    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True #cambiamos el estado a True ya que hay coincidencia
            
    if not found: #con esto controlamos si se actualizo o no el usuario, invertimos el valor de found para forzar la condicion negativa
        raise HTTPException(status_code=404, detail= "El usuario no se encontro para eliminarlo" )
    else:
        return {"se borro el usuario con exito"}
    
    
    