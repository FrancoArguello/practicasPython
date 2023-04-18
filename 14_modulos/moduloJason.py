import json

datos='{"nombre":"Franco", "apellido":"Argüello", "edad": 29, "nombre":"juan"}' #solo admite un valor para una llave, la ultima es la que queda

lecturaDatos=json.loads(datos) #convertimos el dato en un modulo Json

print(lecturaDatos) #obtenemos todos los datos
print(lecturaDatos["nombre"]) #aca obtenemos un dato especifico utilizando lo qu es las llaves/valor como en las librerias



####################################################
#pasar de un Json a String

datosJSON={"nombre":"Franco", "apellido":"Argüello", "edad": 29}

datosJSONString= json.dumps(datosJSON)

print(datosJSONString)