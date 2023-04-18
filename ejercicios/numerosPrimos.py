#crear una funcion que nos devuelva los numeros primos entre 0 y el arguemento que le pasemos
#numeros primos divisibles por 1 y por si mismo


#esta funcion verifica que sea primo
def num_primo(num):  
    for i in range(2, num):#num aca no sufre ninguna modificacion xq no queremos que lo incluya, arranca x el 2 xq todos los numeros son divisibles por 1
        if num%i == 0: return False #si nos da false quiere decir que el numero fue divisible por otros, entronces no es primo
        
    return True # si nos da true quiere decir que no fue divisible por otros numeros entonces  es primo


def primos_hasta(num):
    primos= [] #creamos una lista para ir guardando los numero primos
    for i in range(2, num+1): #le sumamos uno para que incluya el numero indicado por el usuario
        resultado= num_primo(i) #aca invocamos a la funcion y le pasamos el valor de i para que verifique si ese numero es divisible por otros menores o no
        if resultado == True: #si el valor retornado es true quiere decir que es primo
            primos.append(i) #entonces aca lo agregamos a la lista
    return primos
        
        
        
indice =int(input("ingrese hasta que numero desea saber los num perimos que hay entre el 0 y el numero indicado: "))
primos = primos_hasta(indice)
print(primos)


###############################################################3
#resuelto con lambda

primos_hasta= lambda num: list(filter(lambda x: all(x%i !=0 for i in range(2, int(x**0.5)+1)), range(2,num)))
print(primos_hasta(15))