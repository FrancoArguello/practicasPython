# Diferencia entre set y diccionario es que los set contienen informacion como las listas y las tuplas
# y los diccionarios son set que ya utilizan lo que son las claves:valor
######################################################################################
# usar los set como diccionario, con llave valor
# tipo de dato: dict
# tuplas pueden ser claves xq son inmutables
# las listas no pueden ser claves xq son modificables, a no ser que usemos el frozenser()

# forma 1
print("\nuso diccionario llave/valor")
nombres = {
    "nombre": "Franco",
    "ciudad": "Moreno",
    "edad": 29}


print(nombres["nombre"])  # aca acceso al valor de la llave "nombre"

# otra manera de acceder al valor de la llave "nombre" si no se encuentra el programa sigue
print(nombres.get("nombre"))


# forma 2
datos = dict(nombre="Franco", apellido="Argüello")
print(datos)

# forma 3 crear un diccionario vacio

datos = dict()


# crear diccionarios con fromkeys para crear todos los valores en none

diccionario = dict.fromkeys(["nombre", "apellido"])
print(diccionario)
# editar el valor predeterminado y que no sea none
diccionario = dict.fromkeys(["nombre", "apellido"], "no se")
print(diccionario)

''' Si no colocamos las claves en forma de lista nos va a mostrar un error interesante se puede ver esto con el siguiente ejemplo que nos puede servir en otro caso como el el ejemplo 2

diccionario =dict.fromkeys("nombre", "apellido")
print(diccionario)

diccionario =dict.fromkeys("abcder") #nos va a crear todas las clave con cada una de las letras y el valor en none ya que el primer valor que pasamos es iterable y el segundo le indicamos con que valor queremos que se setee
print(diccionario)

'''

######################################################################################
# borrar elementos de un diccionario

print("\nborrar elementos del diccionario")
nombres = {
    "Franco",
    "Thiago",
    "ivana", "Theo"}
nombres.remove("Theo")
print(nombres)
nombres.pop()  # si no esta ordenada el diccionario nos va a borrar el primer elemento que aparesca de manera aleatoria
print(nombres)
nombres.clear()  # nos borra todos los elementos del diccionario
print(nombres)

######################################################################################
# modificar elementos de un diccionario
print("\nmodificar datos de un diccionario")
nombres = {
    "nombre": "Franco",
    "ciudad": "Moreno",
    "edad": 29}

nombres["nombre"] = "Thiago"
nombres["edad"] = nombres["edad"] + 2
print(nombres)

######################################################################################
# agregar informacion a un diccionario
print("\nagregar datos de un diccionario")
nombres = {
    "nombre": "Franco",
    "ciudad": "Moreno",
    "edad": 29}

nombres.update({"apellido": "Argüello"})
# aca le agregamo un set a nuestro diccionario como valor de una clave
nombres.update({"lenguajes": {"python", "javaScript", "php"}})
print(nombres)

######################################################################################
# borrar claves de un diccionario

print("\nborrar clave de un diccionario")
nombres = {
    "nombre": "Franco",
    "ciudad": "Moreno",
    "edad": 29,
    "apellido": "Argüello"}

nombres.pop("apellido")
print(nombres)

######################################################################################
# copiar un diccionario

print("\ncopiar un diccionario")


nombres = {
    "nombre": "Franco",
    "ciudad": "Moreno",
    "edad": 29,
    "apellido": "Argüello"}
print(nombres)

nuevosNombres = nombres.copy()
print(nuevosNombres)

######################################################################################
# hacer un diccionario iterable

diccionario_iterable = nombres.items()

print(diccionario_iterable)


#############################################################
# UNIR diccioanrios
autos = {"1":"chevrolet", "2":"peugeot", "3":"ford", "4":"toyota", "5":"renault", "6":"roll royce"}
autos2 = {"7":"audi", "8" : "Aston Martin"}
#DESEMPAQUETAMIENTO DE ITERABLES
autos = {**autos , **autos2} #con el astericos sacamos todos los elementos del iterable
autos3= {**autos}
print("\n\n")
print(autos3)

