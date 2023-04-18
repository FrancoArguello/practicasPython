
import pandas as pd

########################################################
#Leemos el archivo csv

df=pd.read_csv("manejo_de_archivos\\ejercicios_manejo_de_archivos\\texto1.csv", encoding= "UTF-8")
print(f'{df}\n')

######################################################
#cambiar el tipo de dato de una columna
df['edad'] = df["edad"].astype(str) #--> con el .astype(le cambiamos el tipo de dato)
print(type(df["edad"][0])) #--> con el [0] le decimos que elemento queremos que nos devuelva en pantalla


######################################################
#reemplazar un elemento
print()
df['apellido'].replace("Aquino","Fernandez", inplace = True)
print(df["apellido"][2]) #verifico que Aquino se haya modificado


######################################################
#borrar las filas con datos faltandes
print("\nBorra las filas con datos faltantes\n")
df = df.dropna() #busca la ultima fila con algun dato faltante --> Nan
print(df)



######################################################
#borrar las filas con datos faltandes
print("\nBorra las columnas con datos faltantes\n")
df = df.dropna(axis=1) #con axis borramos la primera columna con algun faltante
print(df)


######################################################
#borar filas que se repiten
print("\nborrar duplicados\n")
df = df.drop_duplicates() #solo me deja uno solo y es el ultimo que se agrego a la lista
print(df)

######################################################
#crear un archivo csv nuevo con los datos limpios
df.to_csv("manejo_de_archivos\\ejercicios_manejo_de_archivos\\df_limpio.csv", encoding= "UTF-8")