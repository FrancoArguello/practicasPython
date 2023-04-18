#son funciones anonimas que se aplican para evitar abrir un bloque de codigo
#beneficios: se pueden usar en acciones sensillas y que necesitamos rapidas,
            #se puede asignar a una variable la funcion y el resultado lo retorna automaticamente
#no son fuiones aptas para mas de una 1 instruccion
# es muy parecid a las funciones flecha --> de JS

#estructura
#variable = palabra reservada lambda + los valores a utilizar + los : y luego que es lo que va a hacer
sumar     =       lambda          primer_valor, segundo_valor:         primer_valor + segundo_valor

print(sumar(1,3)) #-> aca la variable se va a comportar como una funcion, lo printeamos asi para imprimir el valor retornado, sino lo hacemos de esta manera nos va a retornar el onjeto lambda

#usar una funcion lambda dentro de una funcion y pasarle los parametros por la funcion
def sumar_tres_numeros(value):
    return lambda primer_valor, segundo_valor: primer_valor + segundo_valor + value
print(sumar_tres_numeros(5)(2,4))


##################################33
#ej funcion lambda
multiplicar_por_dos = lambda x : x*2

print(multiplicar_por_dos(5))


######################################################
#ejemplo de como optimiza codigo las funciones lambda


def num_par(num):
    if (num%2 == 0):
        return True
        
        
numeros=[1,2,3,4,5,6,7,8,9,10]        
numeros_pares=filter(num_par, numeros) #filter es una especie de bucle que va a recorrer toda la lista elemneto x elemento y va guardando los elementos a una lista
print(list(numeros_pares)) #lo casteamos para que nos muestre la lista creada y no el objeto de filter


#AHORA LO HACEMOS CON UNA FUNCION LAMBDA PARA VER COMO ACHICAMOS CODIGO Y LO HACEMOS MAS EFICIENTE

numeros_pares2=list(filter(lambda numeros:numeros%2==0, numeros))
print(numeros_pares2)