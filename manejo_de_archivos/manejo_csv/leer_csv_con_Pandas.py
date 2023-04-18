#debemos instalar pandas con el cmd como admin
#1ro instalar el pip -->  py -m ensurepip --upgrade
#2do instalat pandas --> py -m install pandas
#3ro importar pandas renombrar por convencion como pd

import pandas as pd

df=pd.read_csv("manejo_de_archivos\\manejo_csv\\texto1.csv", encoding= "UTF-8") #df = dataFrame son archivos que se tratan como hojas de calculos, que tienen filas y columnas
#df=pd.read_csv("manejo_csv\\texto1.csv", encoding= "UTF-8", names =["name", "lastname", "age"]) #asi le decimos como se van a llamar los encabezados

print(df)
#print(df["nombre"]) # de esta manera accedemos a los valores de la columna nombre

#ordenamos el dataFrame por edad
df_ordenado= df.sort_values("edad", ascending=False) #usamos el ascendig=False para ordenarlo de manera descendiente
print(df_ordenado)


########################################33
#concatenar csv
df=pd.read_csv("manejo_de_archivos\\manejo_csv\\texto1.csv", encoding= "UTF-8") 
df2=pd.read_csv("manejo_de_archivos\\manejo_csv\\texto1.csv", encoding= "UTF-8") 

dfs_concatenados = pd.concat([df, df2])
print(dfs_concatenados)


#################################################
#decimos hasta que fila queremos acceder
print()
imprimir_primeras_filas = df.head(3) #con el numer0 entre () le decimos hasta que fila queremos ver, el 0 es el encabezado
print(imprimir_primeras_filas)

imprimir_utimas_filas = df.tail(2) #para ver las ultimas filas
print(imprimir_utimas_filas)


#saber cuantas columnas y filas tiene el archivo con shape
print()
filas_y_columnas = df.shape #nos va  arrojar una tupla donde nos dice la cantidad de filas y columnas totales
print(filas_y_columnas)

filas_totales= filas_y_columnas[0]
print(f'el total de las filas es: {filas_totales}')

columnas_totales = filas_y_columnas[1]
print(f'el total de las columnas es de : {columnas_totales}')

#podemos desempaquetar la cantidad de filas y columnas de la siguiente manera
filas,columnas = df.shape
print(filas) #nos arroja la cantidad de filas
print(columnas) #nos arroja la cantidad de columnas


###########################################3
#acceder a un elemento especifico del df con loc

elemento_espeficio_loc =df.loc[2, "edad"] #con el numero le indicamos que fila, y luego indicamos que columna con su titulo
print(elemento_espeficio_loc)

elemento_espeficio_iloc =df.iloc[3,0] #con el numero le indicamos que fila, y luego indicamos que columna con su indice tambien
print(elemento_espeficio_iloc)

print()
acceder_columna_apellidos= df.iloc[:,1] #accedo a todos los datos de la columna "nombre"
print(acceder_columna_apellidos)

acceder_elementos_de_fila= df.iloc[2,:]  #accedo a todos los datos de la fila 2
print(acceder_elementos_de_fila)



print("accediendo a filas con edad mayor que 30")
mayor_de_30 = df.loc[df["edad"]>30, :]  #no olvidarse la coma xfavorrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr
print(mayor_de_30)