

"""tipo de dato de la lista es LIST"""
provincias = list()
provinciasEliminadas = []
provinList = ["Buenos Aires", "La Pampa", "Rio Negro",
              "Corrientes", "Entre Rios", "Mendoza", "Misiones"]
print(provinList)
print()


# .index() nos informa el indice que tiene un valor de la lista

print(provinList.index("La Pampa"))

# nos informa la cantidad de elementos de la lista
provinList = ["Buenos Aires", "La Pampa", "Rio Negro",
              "Corrientes", "Entre Rios", "Mendoza", "Misiones"]
print(len(provinList))

# acceder a un elemento de un indice determinado
print(provinList[3])

# append sirve para agregar algo al final de la lista
provinList.append("Túcuman")
print(provinList)
print()


# es para borrar un dato de la lista en el orden 2#
del provinList[2]
print(provinList)
print()

# con insert podemos decirle en que posición queremos agregar un dato a la lista, el numero indica el indice en el cual queremos insertar el elemento, pero no sobreescribe si ya hay un elemento en ese indice sino que lo corre de lugar
provinList.insert(2, "Santa Fe")
print(provinList)
print()

# funcion sorted(parametro)
# sorted nos odena la lista de menor a mayor o alfabeticamente solo modifica el orden cuando se ejecuta, no lo modifica definitivamente#
print(sorted(provinList))


# .sort() es un metodo
# nos cambia el orden definitivo de la lista de menor a mayor#
provinList.sort()
print(provinList)
print()


# nos ordena e invierte la lista
provinList.sort(reverse=True)
print(provinList)
print()

# nos invierte el orden de la lista definitivo pero no la ordena como en el sort
provinList.reverse()
print(provinList)


# "del" nos borra utilizando el indice del elemento que deseo borrar
del provinList[-1]
print(provinList)
print()

# es para eliminar el elemento con su indice
# con numeros negativos se va a ir borrando de atras para adelante
elimProv = provinList.pop(2)
print(provinList)
# aca nos va a decir cual fue el elemento eliminado
print("Elemento de la lista eliminado es:", elimProv)
print()


# para eliminar colocando el elemento que deseamos eliminar

# borra el elemento por su valor si no hay ese valor nos arroja un excepcion
provinList.remove("La Pampa")
print(provinList)


# para agregar los elementos de una lista a otra lista o varios elementos usamos el .extend()
print("\npara agregar los elementos de una lista a otra lista o varios elementos usamos el .extend()")
minusculas = ["a", "b", "c"]
minusculas = ["a", "b", "c"]
mayusculas = ["A", "B", "C"]
print(minusculas)
print(mayusculas)

minusculas.extend(mayusculas)
# hay que pasarlo en forma de lista y no elementos sueltos
minusculas.extend(["z", "x"])
print(minusculas)


"""ahora si quiero crear una lista nueva con los datos borrados sin perder registro de este dato hacemos asi"
provinciasEliminadas.append(provinList.pop(2))
print(provinciasEliminadas)
print("Elemento de la lista eliminado es:", provinciasEliminadas)
"""

# para concatenar lsitas hacemos así:
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
concaLis = lista1 + lista2


# Listas de numeros
numeros = [1, 2, 3, 4, 5, 45, 6, 7, 8, 9]
print(max(numeros))  # valor mas alto
print(min(numeros))  # valor mas bajo


# clear nos sirve para borrar todos los datos de una lista

autos = ["chevrolet", "peugeot", "ford", "toyota", "renault", "roll royce"]
print(autos)
autos.clear()
print(autos)
autos.append("rastrogero")
print(autos)

# copiar los elementos de una lista dentro de otra
autos = ["chevrolet", "peugeot", "ford", "toyota", "renault", "roll royce"]
masMarcas = autos.copy()
masMarcas.append("mazda")

print(masMarcas)


###########################
#DESEMPAQUETAMIENTO DE ITERABLES
print(*autos) #con el astericos sacamos todos los elementos del iterable

a,b,c,d,e,f = [*autos] #desempaquetamos el iterable y lo asignamos a distintas variables cada valor

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)