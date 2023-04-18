#son funciones que son capaces de trabajar con otras funciones

def sum_one(value):
    return value + 1

def sum_five(value):
    return value + 5

def sum_two_value_and_add_value(first_value, secund_value, f_sum): #f_sum es la funcion que le vamos a pasar
    return f_sum(first_value + secund_value)

print(sum_two_value_and_add_value(2,5,sum_one))

print(sum_two_value_and_add_value(2,5,sum_five))


#######  CLOSURES ######## cloyers
#hace referencia a las funciones de orden superior pero con la peculiaridad que creamos funciones dentro de funciones
#nos sirven para realizar acciones asincronas para desarrollo de apis o back

#es una funcion  que define una funcion y que nos retorna esa funcion y que al final la ejecuamos como queremos
#no retorna un valor no returna un calculo, retorna una funcion

def sum_ten(original_value): # si aca le ponemos que debemos pasarle un valor este se guarda como contexto de la funcion
    def  add(value):
        return value +10 + original_value
    
    return add

add_crosure = sum_ten(3) # asiganamos la funcion a una variable para capturar el valor retornado que seria una funcion add()
                        #aca lo que hacemos es tener acceso a la funcion add()

#print(add_crosure(5)) #aca a esa funcion que nos retorno en la variable podemos ahora pasarle el parametro a la subfuncion add()
print(sum_ten(3)(5)) #otra manera de llamar a la funcion, primero le pasamos el valor a sum_ten, y luego el valor para add()



# funciones de orden superior que existe ya en Python  ###########################################################################
numeros = [2,5,10,21,100,30]

#########################################
#map()
#map siempre va a utilizar un valor iterable para trabajar
# sirve para pasarle una funcion y que itere una lista y le ejecute esa funcion a cada uno de los elementos
def multiplicar(numero):
    return numero * 2

 
ejemplo_map = map(multiplicar, numeros)

print(list(ejemplo_map)) #si no le cambiamos el tipo de dato nos va a devolver su valor original q es un objeto, al hacer asi vemos el resultado que queremos

#ejemplo con una lambda
print(list(map((lambda x: x*2), numeros)))


#####################################################
#Filter()
#recorre todos los valores y ejecuta una funcion que nos de un  valor true o false para irlos acumulando en una lista y luego restornarnos solo los valores filtrados

#aca definimos la funcion que nos va a retornar los valores true o false
def num_mayores_que_diez(numeros):
    if numeros > 10:
        return True
    return False
    
    
print(list(filter(num_mayores_que_diez, numeros))) #aca nos genera una lista con los valores filtrados

#ejemplo con una lambda
print(list(filter((lambda numero: numero > 10), numeros)))


#########################################
#tenemos que importar el sigueinte modulo
from functools import reduce
#reduce()
#esta fucion opera con un valor mas el acumulado --> basicamente nos va a devolver el total de la suma de todo los valores
def sum_two_values(num1, num2):
    #varificacion del proceso
    print(num1)
    print(num2)
    return num1 + num2



print(reduce(sum_two_values, numeros))

print(sum(numeros)) #--> esto funciona igual pero no tenemos forma de acceder al proceso de la sumatoria