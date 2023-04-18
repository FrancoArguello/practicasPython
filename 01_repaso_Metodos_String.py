cadena1 = "Hoooola, franco, theo, thiago, ivana"
caderan2 = "Hola Franco"

#secuencia de escape de String
info = "Curso de 'Python' " #---> para poner una sola comilla
print(info)
info = 'Curso de "Python" ' #--->mismo casi que el de arriba pero para 2 comillas

info = "Curso de \"Python\" "  #lo que ponemos despues del bash lag es ignorado como un caracter funcional
print(info)



# print(dir(cadena1)) #el dir nos informa el metodo que posee cada tipo de dato en este caso con los str

conv_mayus = cadena1.upper()  # nos convierte todo en mayuscula
conv_min = cadena1.lower()  # nos convierte todo en minuscula
# nos convierte la primera letra en mayuscula y el resto en minuscula
primera_mayus = cadena1.capitalize()
# nos retorna el lugar en la que se encuentra el valor, si no lo encuentra nos va a retornar un -1 el valor
buscar_valor = cadena1.find("o")
# cadena1 = cadena1.index("0") #nos retorna el lugar en la que se encuentra el valor, si no lo encuentra nos va a retornar una excepcion y no un -1 como find
# nos retorna la cantidad de veces que coincide el valor consulado
retorna_coincidencia = cadena1.count("o")

# nos retorna si el string contine  solo numeros
return_si_es_numerico = cadena1.isnumeric()
# nos retorna si el string contine numeros y letras (los espacios son caracteres especiales)
return_si_es_alphanumerico = cadena1.isalpha()
# nos retorna la cantidad de caracteres que tiene
cuenta_catacteres = len(cadena1)

# nos retorna true e false, se fija con que letra/subcadena empieza
empieza_con = cadena1.startswith("H")
# nos retorna true e false, se fija con que letra/subcadena termina
termina_con = cadena1.endswith("f")

# si encuentra el primer valor dado lo reemplaza por el segundo
cadena_nueva = cadena1.replace("hola", "hola maquinola")
# si encuentra el primer valor dado lo reemplaza por el segundo
cadena_nueva2 = cadena1.replace(" ", ",")

# nos devuelve una lista con todos los substring que detecta el sistema que se encuentran separadas por una coma o valor que se le indique entre parentesis
cadena_separada = cadena1.split(",")
print(cadena_separada)
cadena_separada = cadena1.split("o")
print(cadena_separada)
