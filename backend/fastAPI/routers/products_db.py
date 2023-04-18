from fastapi import APIRouter, HTTPException #con api router podemos crear rutas, y con el httpexce... podemos manejas los tipos de status que nos da el server y las excepciones o aviso que queremos que muestre
from pydantic import BaseModel #para definir una identidad

router = APIRouter(prefix="/productsdb",
                   tags= ["productdb"],
                   responses= {404 : {"message" : "no encontrado"}}) #indicamos que va a ser un router-- con el prefix como va a ser su ruta de acceso generica


products_list= ["producto 1",
               "producto 2",
               "producto 3",
               "producto 4",
               "producto 5",
               "producto 6",
               "producto 7"]



@router.get("/") 
async def products():
    return  products_list

@router.get("/{id}")
async def products(id:int):
    return products_list[id]