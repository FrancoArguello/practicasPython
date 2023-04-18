
# estructura de una funcion basica

# operadores in / not in nos arroba un True o False
print("Franco" in "Franco Arguello")
print("Hola" not in "Hola")


### Ejemplo 1 ###
print("\nejemplo 1")


def suma(a, b):  # definimos la funcion y entre () los argumentos que va a recibir la funcion
    # proceso o rutina de la funcion
    c = a+b
    print(f"la suma de los numeros es igual a: {c} ")


# invocacion de la funcion, entre () hay que pasarle los argumentos a nuestra funcion
suma(1, 3)
suma(34, 6)


### Ejemplo 2 ###
print("\nejemplo 2")


def saludar(*nombres):  # con el *no le determinamos la cantidad de parametros que le vamos a enviar

    # con el corchete le enviamos el indice del parametro que debe utilizar,
    nombre = nombres[1]
    #  no hace falta que utilice todos los parametros que le enviamos a la funciones
    print(f"hola {nombre}")


# el indice de los parametros comienza en 0 como en las listas
saludar("franco", "jose", "Thiago")
# 0       1         2
### ejemplo 3 ###
print("\nejemplo 3")

########### Argumentos opcionales

def saludar(nombre, apellido = "Argüello"):  # arguemento con un valor predeterminado
    print(f"hola {nombre} {apellido}")

saludar("thiago")  # si aca no le pasamos ningun parametro va a utilizar el predeterminado para apellido en este caso "Argüello"

saludar("jose", "Perez")  #acá va a utilizar el valor indicado "jose" y "perez" ignorando "argüello"

saludar(apellido = "martinez", nombre = "Martin") #Si no sabemos el orden en cual se pasan los parametros podemos nombrarlos pero en este caso estamos obligados a nombrar todos los parametros, por ej. en este caso no podemos pasarlo asi saludar("martinez", nombre = "jose" )




#######################################################################
#######################################################################

print("")
# funcion para crear contraseña random


def crear_contraseña(num):
    letras = "qwertyuiop"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num-5
    contraseña = f"{letras[c1]}{letras[c2]}{letras[c3]}{num*2}"
    print(contraseña)


crear_contraseña(8)  # uor16


# funciones que retornan un valor para usarlo despues usarlo fuera de la funcion

def crear_contraseña(num):
    letras = "qwertyuiop"
    num_entero = str(num)
    # "se queda con el primer numero del numero que le pasamos ej 34 solo se queda con el 3"
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num-5
    contraseña = f"{letras[c1]}{letras[c2]}{letras[c3]}{num*2}"
    return (contraseña)


password_nuevo = crear_contraseña(70)  # yie14
print(f'el password creado es: {password_nuevo}')

# utilizando el parametro args *
########
# opcion1
print("\n\n")


def sumar(*numeros): #con el * indicamos que el argumento va a ser un iterable
    resultado = sum(numeros)
    return resultado


resultado = sumar(1, 2, 3, 4)
print(resultado)

########
# opcion 2  mas optima en terminos de computos y corta


def sumando(numeros):
    return f"el resultado es {sum([*numeros])}"


resultado2 = sumando([1, 2, 3, 4])
print(resultado2)

'''
verificacion de porque no siempre es lo mas optimo a termino de usabilidad a futuro
X = resultado2
print (X + 10)

'''


##########################################
print()
####### Kwargs
def get_productos(**datos): # **significa que va a recibir una cantidad de argumentos indefinidos
    #asi podemos ver el valor asignado a cada clave
    for i in datos:
        print(datos[i])
        
    #así vemos el nombre de las claves de asignación    
    for i in datos:
        print(i)

get_productos(id = 23, nombre = "celular", marca = "Sansung" ) #Si o si hay que nombrar al argumento que se pasan, no se pueden pasar argumentos sin asignarlos previamente a un valor



print()
###################################3
'''Alcance de variables
las variables creadas dentro de las funciones son de alcance local y no puden ser accedidas desde afuera de la función

las variables globales son aquellas que fueron declaradas por fuera de todas las funciones
la utilizacion de las variables globales son una mala practica porque nos podemos modificar un valor sin querer y luego se nos complica encontrar que variable es la que nos esta rompiendo el soft, por eso se deben crear variables solo dentro de su entorno de ejecución
Ejemplo de trabajar con variables globales'''

variable = "Variable Global"

def cambiar_tipo():
    global variable
    variable = "asi modificamos la variable global"
    
print(variable)
cambiar_tipo()
print(variable)