# status nos sirve para trabajar con los estados de http
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel  # para definir una identidad
# OAPass se va a encargar de autenticar el paswword con el usuario
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
# OAPass..RequestFrom es la forma en la que se va a enviar a nuestra api o back el usuario y la contraseña para verificar si corresponden a los datos de nuestra DB
from jose import jwt, JWTError
from passlib.context import CryptContext
# importamos el modulo datetime para trabajar con fechas y horas, y timedelta para hacer calculos de tiempo
from datetime import datetime, timedelta

# openssl rand -hex 32 --> esto lo ponemos en la consola de python para que nos genere un random de 32 hexagesimal
ALGORITMO = "HS256"
ACCESS_TOKEN_DURATION = 1
SECRET = "90dc99771ece7816fb91282d3a34ac05aa634ede6a04cf83ed1c3da9d9955806"

router = APIRouter()
# le pasamos con el tokeUrl la Url por donde le vamos a pasar los datos de user and pass
oauth2 = OAuth2PasswordBearer(tokenUrl="login")
crypt = CryptContext(schemes=["bcrypt"])


class User(BaseModel):  # BaseModel nos da la capacidad de crear una ideantidad
    username: str
    full_name: str
    email: str
    disabled: bool


class UserDB(User):  # heredamos todos los datos de usuario y le agregamos el pass para guardarlo en la dataBase para si hay que retornar los datos del  usuario por algo no nos retorne su info de autenticacion
    password: str


# Simulacion de una DataSet
users_db = {
    "francoDev": {
        "username": "francoDev",
        # bcrypt generator en la web para generar este hash
        "password": "$2a$12$0SUvSERkxSvOirX4osV5rOXpf6eFDu9tpfPP6gtCBReP2gNyvNkr2",
        "full_name": "Franco Argüello",
        "email": "francoarguello.dev@gmail.com",
        "disabled": False,
    },
    "ivanaDev": {
        "username": "ivanaDev",
        "password": "$2a$12$jihVeP2L4ZJXzRmWE07rv.51UWyJg9CLt7oK4FIcXQ/rtA18z5aDu",
        "full_name": "Ivana Aquino",
        "email": "ivana@gmail.com",
        "disabled": True,
    }
}


def buscar_usuario_db(username: str):
    if username in users_db:  # recorremos la DB con el nombre de usuario
        # retornamos el usuario, cremos un objeto con UserDB() y adentro le pasamos la DB y el parametro que seria username que capturo los datos
        return UserDB(**users_db[username])


def buscar_usuario(username: str):
    for username in users_db:
        return User(**users_db[username])
    # Los ** significa que puede recibir varios parametros


async def outh_user(token: str = Depends(oauth2)):

    exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                              detail="credenciales de autenticacion invalidas",
                              headers={"www.authenticate": "Bearer"})

    try:
        username = jwt.decode(token, SECRET, algorithms=[ALGORITMO]).get("sub")
        if username is None:
            raise exception

    except JWTError:
        raise exception

    return buscar_usuario(username)


async def usuario_actual(user: str = Depends(outh_user)):
    if user.disabled:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Usuario inactivo")
    return user


@router.post("/login")  # como vamos a enviar y recibir info usamos el post
# capturamos la info del usuario con la plantilla del form que tomamos del OAth.... requestForm que importamos y que el form va a venir directo del depends()
async def login(form: OAuth2PasswordRequestForm = Depends()):
    # el depends() significa que va a recibir datos pero que no va a depender de nadie solo de la funcion que le indiquemos

    # El usuario lo recibimos por el form y lo buscamos en la DB con la funcion
    user = buscar_usuario_db(form.username)

    # primero le pasamos el pass que recibimos por el form y segundo el pass que en el obj user creado con los datos de la dataBase
    if not crypt.verify(form.password, user.password):
        raise HTTPException(
            status_code=400, detail="El password no es correcto")  # si no coinciden los datos lanzamos la excepcion

    access_token = {"sub": user.username,
                    # --> nos va a generar un delra con el tiempo actual mas un minuto
                    "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_DURATION)
                    }  # --> nos va a generar un delra con el tiempo actual mas un minuto

    return {"access_token": jwt.encode(access_token, SECRET, algorithm=ALGORITMO), "token_type": "Bearer"}
# el access_token debe ser algo encriptado que solo el back entiende, este token es reenviado constantemenete al back para decirle que sos vos y no tener la necsidad de estar autenticandonos a cada instante o accion que querramos realizar
# con el jwt.encode() encriptamos al token, le pasamos primero el token, despues lo encriptamos con la clave secreta, y usamos el algotirmo para volverlo a encriptar.


@router.get("/users/me")
async def me(user: User = Depends(usuario_actual)):
    return user
