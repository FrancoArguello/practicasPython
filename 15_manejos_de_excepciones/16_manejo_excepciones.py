from time import sleep


def sumar():

    while True:  # ejecuta esto siempre
        print("Ingrese solo números enteros")
        a = input("ingrese un numero: ")
        b = input("ingrese otro número: ")

        try:  # setencia para decirle al programa intenta esto a ver si sale o no una excepcion
            resultado = int(a) + int(b)

        except Exception as e:  # si sale una excepción hace esto y comienza nuevamente el bucle
            # Exception es la clase padre de todas las excepciones que hay en el lenguaje
            # e es la manera de renombrar a una excpecion
            print(
                "no se pueden ingresar letras, caracteres especiales ni numeros que no sean enteros")
            # aca nos dice cual es la excepcion y en donde
            print(f"error: {e}")
            # aca nos dice el nombre del error, con esto podemos saber como tratar mejor la excepcion
            print(f"nombre del error: {type(e).__name__}")

            # ahora si no salto una excepcion no pasa x aca y sale del bucle o continua el proceso segun corresponda
        else:
            break  # si no nos sale una excepcion corta el proceso de ejecucion que siga mas adelante
        finally:  # El finally siempre se va a ejecutar sin importar el proceso o que haya algun break antes
            print("esto siempre se ejecuta sin importar el proceso anterior")
            sleep(2)

    return (f'El resultado de la suma es: {resultado}')


print(sumar())
