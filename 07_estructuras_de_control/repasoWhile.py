contador = 0

while contador < 10:
    contador = contador + 1
    print(contador)

# el bloque de codigo siempre que se cumpla la condicion del while


clave = input("ingrese un numero: ")

while True:
    if int(clave) == 12:
        print("ok")
    if int(clave) != 12 and contador < 4:
        print("chau")
