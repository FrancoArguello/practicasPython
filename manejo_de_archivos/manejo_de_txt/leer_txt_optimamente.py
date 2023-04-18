# con el with open no debemos cerrar el archivo, ya que cuando se ejecuta el codigo se abre y se cierra automaticamente cuando finaliza el proceso
#el with nos trae mas opciones de exceptciones


with open("manejo_de_archivos\\manejo_de_txt\\texto2.txt", encoding= "UTF-8") as archivo: #usamos el as para asignarle un nombre al elemento leido almacenarlo y luego decirle al sistema que queremos que haga 
    contenido = archivo.read() #ese valor temporal lo asignamos a una variable
    print(contenido) 
    