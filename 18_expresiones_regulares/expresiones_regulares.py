#import redis es la libreria externa mas utilizada para el manejo de expresiones regulares
import re #biblioteca estandar de python para manejo de expresiones regulares nativo del lenguajes


#las expresiones regulares busca patrones dentro de algo osea busca coincidencias
#las expresiones regulares sirven para buscar coincidencias de algo q buscamos dentro de una cadena de texto por ejemplo.

texto ='''Hola ..1.  
hola maestro como estas, esta es la cadena 1234 .
hola Esta es la segunda linea de texto $% .... jossose
este es el final de esta oracion 568745. jose
--__
estamos todos locos $% jose'''

match =re.match("Hola", texto) #nos busca si la cadena de texto comienza con lo que le pasamos, nos devuelve de donde hasta donde esta ubicada la coincidencia <re.Match object; span=(0, 4), match='Hola'> ----> span es la ubicacion de los caracteres de coincidencia
print(match)
start, end = match.span() #con span, capturamos los valores de inicio y fin de las posiciones del texto buscado, desempaquetamos la info con 2 variables
print(texto[start:end]) #aca imprimimos el valor de match para ver el texto
print("..........................")

#re.findall() --> nos trae todos los valores que coincidan con la busqueda
#re.search() --> nos trae solo el primer valor que coincida, el resto es ignorado
#re.sub("coincidencias", "nuevo_valor", donde_buscar) --> nos va a reemplazar todas las coincidencias que encuentre por un nuevo valor en el texto o lugar donde esta buscando

#haciendo una busqueda simpre
resultado = re.search("jose", texto) #te busca el "jose dentro de toda la cadena de texto"
print(resultado)

resultado = re.findall("esta", texto) #nos devuelve todas las veces que aparace el conjunto de caracteres de "esta" // aca diferencia entre mayusculas y minusculas
print(resultado)

resultado = re.findall("esta", texto, flags = re.IGNORECASE) #nos devuelve todas las veces que aparace el conjunto de caracteres de "esta" sin importar las mayusculas o minusculas
print(resultado)

print("\nrealizando busquedas regulares")
#\d -> busca digitos numericos del 0 al 9
resultado = re.findall("\d", texto) #nos va a traer todos los numeros que aparezcan en el texto
print(resultado)

#\D -> busca digitos no numericos y saltos de linea
resultado = re.findall("\D", texto) #nos va a traer todos los caracteres no numericos
print(resultado)

print()
#\w -> busca digitos alfanumericos, del 0-9 y el _
resultado = re.findall("\w", texto) #
print(resultado)


print()
#\w -> busca digitos no alfanumericos,espacios y saltos de linea ->\n
resultado = re.findall("\W", texto) #
print(resultado)


print()
#\s -> busca espacios en blanco, tabs, y saltos de linea
resultado = re.findall("\s", texto) #
print(resultado)

print()
#\S -> busca los que no son espacios en blanco, tabs, y saltos de linea
resultado = re.findall("\S", texto) #
print(resultado)

print("")
#"\."" -> busca los puntos
resultado = re.findall("\.", texto) #
print(resultado)

print("")
#r"."" -> busca todo menos los saltos en linea
resultado = re.findall(r".", texto) #
print(resultado)

print("")
#"\n"" -> busca los saltos en linea
resultado = re.findall("\n", texto) #
print(resultado)

print("^texto busca coincidencia con el comienzo de la cadena")
#^texto busca el comienzo de la cadena
resultado = re.search("^Hola", texto) #esto por defecto solo nos busca en la primera palabra del texto total
print(resultado)

resultado = re.findall("^hola", texto,flags=re.M) # M de multilinea ->esto nos busca en cada primera palabra de cada renglon y sin diferencias mayus de min
print(resultado)

print("")
print("texto$ busca el fin de la cadena")
resultado = re.findall("jose$", texto,flags=re.M ) #esto por defecto solo nos busca en la primera palabra del texto total
print(resultado)

print("")
#{n} busca n cantidad de veces el valor de la izquierda
resultado = re.findall(r'\d{3}', texto) #-> nos va a buscar 3 numeros que esten escritos seguidos uno del otro
print(resultado)

print("")
#{n,m} busca concidencias en un rango de valores como minimo tanto como maximo tanto
resultado = re.findall(r'\d{4,6}', texto)
print(resultado)

#buscar concidencia con de letras
resultado = re.findall(r'os{2,3}', texto) #-> nos va a traer todas las veces que aparezca una o seguida de una s al menos una vez y maximo 3 veces que se repita la s
print(resultado)

#buscar concidencia con de letras
resultado = re.findall(r'[os]{2}', texto) #-> nos va a traer todas las veces que aparezca la os juntos
print(resultado)


print("propiedad | --> O")
#propiedad | busca o una cosa o la otra
resultado = re.findall(r'\d{2,4}|Hola', texto) #-> el resultado nos lo va a mostrar a medida que vaya apareciendo en el texto las coincidencias buscadas
print(resultado)

#armando expresiones regulares de busqueda
#armando una cadena que busque un numero, seguido de un punto y un espacio

print("\ncombinacion de expresiones")
resultado = re.findall(f'\d\.\s', texto)
print(resultado)

resultado = re.findall(r'\d{3}\s', texto) #-> nos va a buscar 3 numeros que esten escritos seguidos uno del otro y con un espacio despues del 3er numero
print(resultado)




