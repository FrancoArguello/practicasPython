######################################################################################
# iterar set, listas y tuplas es de la misma manera

animales = ["perro", "gato", "elefante", "leon"]
numeros = {1, 3, 5, 78}


# recorremos la lista animales
for i in animales:
    print(i)

# recorrer dos listas o más a la vez, para esto la cantidad de elementos que contienen las listas deven ser iguales
# para esto necesitamos utilizar la funcion zip()
for i, j in zip(animales, numeros):
    print(f'recorrinedo lista 1: {i}')
    print(f'recorrinedo lista 2: {j}')

for i in range(1, 10):
    print(i)

# como recorrer una lista con su indice

for numero in enumerate(numeros):
    print(numero)  # aca nos va a retorar en pantalla dos valores ej(3,78) el 3 es el indice, y el 78 el valor del elemento ubicado en la posicion 0


# for/else  el else siempre se ejecuta al momento de terminar de iterar el for
for animal in animales:
    print(animal)
else:
    print("finalizo el iterado")


frutas = ["anana", "banana", "melon", "frutilla", "aceituna", "sandia"]

for fruta in frutas:
    if fruta == "banana":
        continue  # El continue permite seguir con el iterado sin tener en cuenta el valor
    print(f"me voy a comer una {fruta}")

    if fruta == "aceituna":

        break  # finaliza todo el bucle y no se ejecuta ninguna sentencia posterior a esta sentencia ni siquiera el else
else:
    print("finalizo el bucle")


# recorrer un String

nombre = "franco"

for letra in nombre:
    print(letra)

##################################
# HACER UN FOR EN UNA SOLA LINEA
# caso largo
numeros = [2, 4, 6, 8]
numeros_duplicados = list()

for numero in numeros:
    numeros_duplicados.append(numero*2)


print(numeros_duplicados)

# caso corto
numeros_duplicados = [numero*2 for numero in numeros]
print(numeros_duplicados)
######################################################################################
# recorrer un diccionario
datos = {
    "nombre": "Franco",
    "ciudad": "Moreno",
    "edad": 29}

for dato in datos.items():
    clave = dato[0]
    valor = dato[1]
    print(f'La clave es: {clave} y el valor es: {valor}')
