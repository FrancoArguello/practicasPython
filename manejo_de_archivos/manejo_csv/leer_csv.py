#los archivos csv son archivos separados por comas y delimitados por comillas ""
# los csv se separan valor coma valor espacio en linea --> " "," "," "\n 
#                     " "    ,  "   "    \n

import csv #importamos la libreria de csv para trabajar mejor los csv



#LEER UN CSV
#ejemplo 1
with open("manejo_de_archivos\\manejo_csv\\texto1.csv",  encoding= "UTF-8") as datos:
    info = csv.reader(datos) #leer el archivo
    
    for row in info: #con este for iteramos columnas por columnas
        print(row)       
datos.close()


#ejemplo 2
with open("manejo_de_archivos\\manejo_csv\\texto2.csv", encoding= "UTF-8") as ruta:
    for row in ruta.readlines():
        print(row)
        

#ESCRIBIR EN UN CSV #######################################################
with open("manejo_de_archivos\\manejo_csv\\texto2.csv","w+",  encoding= "UTF-8") as ruta:
        datos = csv.writer(ruta)
        datos.writerow(["color","animal","numero"])
        datos.writerow(["rojo","leon",14])
        datos.writerow(["verde","loro",22])



