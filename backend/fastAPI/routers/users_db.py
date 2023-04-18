# -*- coding: utf-8 -*-

# con api router podemos crear rutas, y con el httpexce... podemos manejas los tipos de status que nos da el server y las excepciones o aviso que queremos que muestre
from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel  # para definir una identidad
from db.models.models_user import User
from db.client import db_client
from db.schemas.schemas_user import user_schema, users_schema
from bson import ObjectId


router = APIRouter(prefix="/usersdb",
                   tags=["usersdb"],
                   responses={status.HTTP_404_NOT_FOUND: {"message": "no encontrado"}})  # indicamos que va a ser un router-- con el prefix como va a ser su ruta de acceso generica, con tags indicamos como va a aperecer en nuestra documentacion, y responses es el mensaje que va a mostrar en el caso de que falle el ingreso a esta ruta


############################  FUNCIONES DE BUSQUEDA  #####################################

# funcion para buscar un usuario por id
def search_user(field: str, key: str):

    try:
        user = db_client.users.find_one({field: key})
        return User(**user_schema(user))
    except:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            detail="No se ha encontrado el usuario")


# funcion para buscar un usuario por su email
def search_user_by_email(email: str):

    try:
        user = db_client.users.find_one({"email": email})
        return User(**user_schema(user))
    except:
        pass


#########################  MOSTRAR TODOS LOS USUARIOS ########################################

# aca nos crea un json automaticamente, nos muestra nuestra base de Datos
@router.get("/", response_model=list[User])
async def users():
    return users_schema(db_client.users.find())


#####################  BUSCAR UN USUARIO POR ID  ##############################################
# entre llaves ponemos el parametro que queremos captuar e interpretar -->puede ser id, name, mail, etc
@router.get("/{id}")
async def user(id: str):
    return search_user("_id", ObjectId(id))


####################  CREAR UN USUARIO #################################

@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def user(user: User):  # le pasamos como parametro un usuario de tipo Useer
    if type(search_user_by_email(user.email)) == User:
        # cuando lanzamos un error tenemos que usar un raise no un return
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            detail="Ya tenemos un usuario registrado con el mismo email")

    users_dict = dict(user)

    # borramos para que no se inserte el id y esto lo haga automaticamente MongoDB --> _id
    del users_dict["id"]

    # aca le insertamos el Id con el que se creo
    id = db_client.users.insert_one(users_dict).inserted_id

    # aca transformamos los datos en un Json
    new_user = user_schema(db_client.users.find_one({"_id": id}))
    return User(**new_user)


#####################  ACTUALIZAR UN USUARIO ######################################
# put usamos cuando vamos a actualizar el total de la info
@router.put("/", response_model=User)
async def user(user: User):

    user_dict = dict(user)
    del user_dict["id"]

    try:
        db_client.users.find_one_and_replace(
            {"_id": ObjectId(user.id)}, user_dict)
    except:
        return {"El usuario no se encontro para modificarlo"}

    # si se actualizo nos retorna el usuario modificado
    return search_user("_id", ObjectId(user.id))


########################## BORRAR UN USUARIO ###################################
# para borrar un usuario
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def user(id: str):
    found = db_client.users.local.find_one_and_delete({"_id": ObjectId(id)})

    if not found:  # con esto controlamos si se actualizo o no el usuario, invertimos el valor de found para forzar la condicion negativa
        return {"error": "No se ha eliminado el usuario"}
