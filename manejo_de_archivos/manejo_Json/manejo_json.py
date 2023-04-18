import json #nos sirve para poder trabajar con Json


archivo = open("manejo_de_archivos\\manejo_json\\archivo.json", "w+", encoding= "UTF-8")  #aca nos crea siempre el archivo y lo sobreescribe

json_test= {
    "nombre":"Franco",
    "apellido": "Arguello",
    "ciudad": "Moreno", 
    "edad":29,
    "nacionalidad": "argentina"
    }

json.dump(json_test, archivo, indent=1) #de esta manera escribimos en el Json, primero le pasamos la informacion, y luego la ruta de acceso al archivo(fp), con el ident le decimos cuantos espacios queremos delante de la llave y ver todo en forma de columna y no en fila.

#json.dump(json_test, archivo) cada dump que llevamos a cabo nos agrega la info en el lugar donde queda el punte en el Json

with open("manejo_de_archivos\\manejo_json\\archivo.json", "w+", encoding= "UTF-8") as archivo:
    for line in archivo.readlines():
        print(line)
   


json_contenido = json.load(open("manejo_de_archivos\\manejo_json\\archivo.json")) #de esta manera pasamos de un Json a un diccionario en Python y podemos trabajarlo como tal
print("\n\ncontenido del Json")
print(f"\n{json_contenido}")
print(json_contenido["nombre"]) #accedemos a la clave del diccionario
