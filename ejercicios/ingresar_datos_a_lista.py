"""Crear una app que le pida al usuario que cantidad de numeros quiere guardar en una lista
"""

cantNumeros=int(input("Ingrese la cantidad de números que desea agregar a la lista: "))
contador=1
listNumeros=[]

if cantNumeros<contador:
    print("no se pueden pedir números menores a 1")
else:
    while contador<=cantNumeros:
        nuevoNumero=int(input("ingrese el número que desea agregar a la lista en la posición " + str(contador) +" : "))
        listNumeros.append(nuevoNumero)
        contador=contador+1


print(listNumeros)