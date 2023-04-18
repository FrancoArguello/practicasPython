# los set son colecciones de datos, se pueden usar como diccionarios
# los set pueden contener diferentes tipos de datos. int, str,bol, tuple
# las listas y diccionarios no dejan agregar a los set ya que es un elemento modificable y los set solo permiten alementos que no puedan ser modificados
# ls set no admiten elementos duplicados
# no se puede acceder a un elemento por el indice
# son un conjunto de datos desordenadors


a = [1, 34]
b = (34, 54)
# anana no va a aparecer 3 veces sino solo una, el resto se borran
frutas = {"manzana", "anana", "pera", b, "anana", "anana"}
print(frutas)
# print(frutas[3]) #no funciona se puede acceder a un set con un for asignandole un valor a cada valor con la variable de iteración.
print(type(frutas))


######################################################################################
# agregar un elemento al set

newFruit = "mandarina"
frutas.add(newFruit)
print(frutas)

######################################################################################
# unir set

frutas_verdes = {"limon", "lima", "manzana verde"}
frutas_rojas = {"frutillas", "manzana roja", "frambuesa"}
frutas_verdes.update(frutas_rojas)
print(frutas_verdes)


# re asignamos mismo valor a la variable para el ejemplo
frutas_verdes = {"limon", "lima", "manzana verde"}
frutas_Ricas = frutas_verdes.union(frutas_rojas)
print("\nfrutas Ricas:")
print(frutas_Ricas)

#################################################
# para poder agregar un conjunto de datos modificables (lista, diccionario) usamos la funcion frozenset
# esta funcion va a hacer que ese conjunto que puede variar sea inmuable ahora y pr lo tal los set lo van a permitir
'''
ASI NOS DARIA ERROR
conjunto_numeros= [1,2,3]

set1= {34,45,67}

new_set= {"hola", "mundo", conjunto_numeros}

print(new_set)
'''

# manera correcta
conjunto_numeros = frozenset[1, 2, 3]

set1 = {34, 45, 67}

new_set = {"hola", "mundo", conjunto_numeros}

print(new_set)


# teoria de conjuntos

conjunto1 = {1, 2, 3, 4, 5, 6}
conjunto2 = {3, 6}


# dos formas de verificar si es un subconjunto
# forma1
# nos arroja un tru xq el conjunto 2 esta incluido en el conjunto 1
resultado = conjunto2.issubset(conjunto1)
print(resultado)

# froma2
# nos arroja false xq no esta incluido ya que contiene mas datos
resultado = conjunto1 <= conjunto2
print(resultado)


# dos formas de verificar si es un superconjunto
# forma1
# nos arroja un false xq el conjunto 1 no sta incluido en el conjunto 2
resultado = conjunto2.issuperset(conjunto1)
print(resultado)

# froma2
resultado = conjunto1 > conjunto2
print(resultado)


# verificar si los conjuntosno tienen nada que ver entre si
conjunto3 = {0, 345}

resultado = conjunto3.isdisjoint(conjunto1)
# nos va a mostrar TRUE cuando los conjuntos no contienen ningun elemento en comun
print(resultado)
