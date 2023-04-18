# las tuplas no admiten agregar elementos ni quitar
# se ueden crear asi tambien las tuplas
# utilizan la memoria del sistema de una manera mas optima, se recomiendan utilizar con listas de datos que no se van a mdoificar que solo van a ser de lectura.

marcasDeAutos = ("chevrolet", "peugeot", "ford", "roll royce", "mazda")
print(marcasDeAutos)

# se pueden crear asi tambien las tuplas sin parentesis, el sistema solo lo crea
# si colocamos al final una coma indicamos al sistema que va a ser una tupla
tupla = "franco",
nombres = "franco", "thiago", "ivana"

print(type(nombres))
print(type(tupla))


# para acceder a un elemento por su indice
print(marcasDeAutos[-1])

# agregar un elemento a un tupla

listMarcasAutos = list(marcasDeAutos)  # convierto la tupla en una lista
listMarcasAutos.append("VW")  # agrego un elemento a la lista
# print(type(listMarcasAutos))
# convierto la lista en tupla nuevamente casteandolo
marcasDeAutos = tuple(listMarcasAutos)
print(marcasDeAutos)
# print(type(marcasDeAutos))

# desempaquetado de datos de tuplas
# aca tienen que haber la misma cantidad de variables que de elementos (concordancia de datos) o colocar un * en el ultimo elemento para que se asigne una nueva tupla a esa variable
(marca1, marca2, *marca3) = marcasDeAutos

print(marca1)
print(marca2)
print(marca3)


# union de tuplas
modelosAutos = ("amarok", "creze", "corolla", "phantom")

newTupla = marcasDeAutos+modelosAutos
print(newTupla)

# multiplicar la cantidad de elementos de una tupla
print(modelosAutos*3)
