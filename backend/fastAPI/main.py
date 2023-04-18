# -*- coding: utf-8 -*-

from fastapi import FastAPI  # importamos fastAPI
from routers import users, products, autenticacion_jwt, autenticacion_basica, users_db, products_db
from fastapi.staticfiles import StaticFiles
# de la carpeta routers importame los archivos users, products

app = FastAPI()  # instanciamos FastAPI

# routers
app.include_router(users.router)
app.include_router(products.router)
app.include_router(autenticacion_jwt.router)
app.include_router(users_db.router)
app.include_router(products_db.router)
# app.include_router(autenticacion_basica.router)

# incluir recursos estaticos a nuestr api
# con esta url podes acceder a la img http://127.0.0.1:8000/statics/img/foto.png
app.mount("/statics", StaticFiles(directory="statics"), name="statics")


@app.get("/")  # con esto accedemos al contexto de FastAPI, es la raiz de la IP donde se este dezplegando la api, solo una vez se debe utilizar "/"
async def root():  # siempre que llamamos a un servidor la funcion debe ser asincrona para evitar q nuestra app se bloquee mientras hace otro proceso
    return "Este es el Main de mi API!"
