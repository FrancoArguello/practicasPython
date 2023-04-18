with open("manejo_de_archivos\\manejo_de_txt\\texto45.txt", 'a',  encoding= "UTF-8") as archivo:  #con la 'a' le decimos al sistema que vamos a agregar info a el texto, y si no existe el fichero lo crea
    for i in range(5):
        archivo.write(f'Fruta {i+1} agregada\n')
        
        
        
with open("manejo_de_archivos\\manejo_de_txt\\texto45.txt", encoding= "UTF-8") as archivo: #usamos el as para asignarle un nombre al elemento leido almacenarlo y luego decirle al sistema que queremos que haga 
    contenido = archivo.read() #ese valor temporal lo asignamos a una variable
    print(contenido) 
    