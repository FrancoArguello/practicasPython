with open("manejo_de_archivos\\manejo_de_txt\\texto2.txt", 'w',  encoding= "UTF-8") as archivo:  #con el 'w' le decimos al sistema que vamos a modificar el texto, y si no existe el fichero lo crea
    #archivo.write("te sobreescribi todo, salame") #asi nos reescribe todo el archivo, no la agrega a lo que teniamos y perdimos toda la info anterior
    
    archivo.writelines(" hola josesito, pepe") #solo admite archivos iterables
    
    #pasar una lista
    archivo.writelines(["\nhola josesito,\npepe\n", "1\n", "maestro\n"])
    
    #EL WRITELINES Y EL WRITE NOS RESSCRIBRE SIEMPRE EL ARCHIVO PERDIENDO LA INFO ANTERIOR
    
    
with open("manejo_de_archivos\\manejo_de_txt\\texto2.txt", encoding= "UTF-8") as archivo: #usamos el as para asignarle un nombre al elemento leido almacenarlo y luego decirle al sistema que queremos que haga 
    contenido = archivo.read() #ese valor temporal lo asignamos a una variable
    print(contenido) 
    
    