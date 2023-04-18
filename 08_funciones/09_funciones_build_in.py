#estas son las funciones que ya vienen integradas a Python

#max, min, round, lower, append, filter etc

#funcion bool() nos devuelve false si le pasamos un 0, none, false, vacio, y true si es algun valor distinto
resultado_bool= bool([])
print(resultado_bool) #nos da false

#funcion all() nos returna true si todos los valores son verdaderos y false cuando  hay algun elemento 0, none, vacio, false

resultado_all= all([1, [2,3], "franco"]) #hay que pasar una lista o tupla
print(resultado_all) #nos da true

resultado_all= all([0, [2,3], "franco"]) #hay que pasar una lista o tupla
print(resultado_all) #nos da false

#funcion sum nos suma todos los valores de un iterable del mismo tipo
numeros=[1,2,3]
suma_total=sum(numeros)
print(suma_total)
