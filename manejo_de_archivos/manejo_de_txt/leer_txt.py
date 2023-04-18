#alt +shift cambia idioma de teclado

########################################################
#ASI SE ABREN LOS ARCHIVOS Y SE LOS LEE

archivo_sin_leer = open("manejo_de_archivos\\manejo_de_txt\\texto.txt", "r", encoding= "UTF-8") #aca le damos la ruta de acceso al archivo, con "r" le decimos que lo vamos a leer solamente, con r+ leer y escribir

# si usamos "w+" le decimos que aparte de escribirlo y poder leerlo

archivo= archivo_sin_leer.read(7) #con la funcion .read() podemos leer todo el archivo o la cantidad de caracteres indicados

#UNA VEZ QUE SE ABRE EL ARCHIVO POR CUESTIONES DE SEGURIDAD NO SE LO PUEDE VOLVER A ABRIR SIN ANTES CERRARLO
print(archivo)
print() 
archivo_sin_leer.close() # con .close() cerramos el archivo


######################################################

archivo_sin_leer = open("manejo_de_archivos\\manejo_de_txt\\texto.txt", encoding= "UTF-8") #si queremos volver a usar el archivo hay que volverlo a abrir
#aca leemos todas las lineas del texto
texto_completo = archivo_sin_leer.readlines()
print(texto_completo)

archivo_sin_leer.close() # con .close() cerramos el archivo


######################################################
archivo_sin_leer = open("manejo_de_archivos\\manejo_de_txt\\texto.txt", encoding= "UTF-8") #si queremos volver a usar el archivo hay que volverlo a abrir
#aca leemos todas las lineas del texto
linea1 = archivo_sin_leer.readline() # si no indicamos un numero nos devuelve toda la primera linea // si le indicamos un numero nos devuelve esa cantidad de caracteres que pueda llegar a tener la primera linea de texto

print("\nultimo ejemplo")
print(linea1)


archivo_sin_leer.close() # con .close() cerramos el archivo





 