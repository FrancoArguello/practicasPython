'''
Falto el profesor y los alumnos van a armar la clase
PEDIR NOMBRE Y EDAD DE TODOS Y SU EDAD
EL MAS GRANDE ES EL PROFESOR
Y EL MENOR EL AYUDANTE
IMPRIMIR QUIEN ES EL PROFESOR Y QUIEN EL AYUDANTE
'''
import os
from time import sleep

def limpioPantalla():
	sisOper = os.name
	if sisOper == "posix":   # si fuera UNIX, mac para Apple, java para maquina virtual Java
		os.system("clear")
	elif sisOper == "ce" or sisOper == "nt" or sisOper == "dos":  # windows
		os.system("cls")
  
  
def obtener_compañeros(cantidad):
    #limpioPantalla()
    compañeros=[]
    for i in range(cantidad):
        nombre= input("ingrese su nombre :")
        edad= int(input("ingrese su edad: "))
        compañero= (nombre, edad)
        compañeros.append(compañero)
    compañeros.sort(key=lambda x:x[1])  #el sort ordena de menor a mayor
    asistente =compañeros[0][0]
    profesor = compañeros[-1][0]
    
    return asistente, profesor


asistente, profesor = obtener_compañeros(3)
print(f"El profesor va a ser {profesor} y su asistente es {asistente}")
sleep(5)
limpioPantalla()