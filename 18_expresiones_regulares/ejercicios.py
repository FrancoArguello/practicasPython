import re
#############################
texto = "hola buen dia"

encriptado = re.sub("[aeiou]", " * #", texto) #--> al ponerlo entre corchetes le decimos que busque cada una de las letras

print(encriptado)


##################################
texto = "francoarguello_dev@gmail.com"
mail_trucho ="franco arguello@gmail"
patron = "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}" #podemos asignar el patron a una variable para despues utilizarlo
        #buscame letras o numeros sin espacios ni \n seguidos de un @ seguido de letras seguido de un punto seguido de como minimo 2 letras

resultado = re.match(patron, texto)
resultado2 = re.match(mail_trucho, texto)

if resultado:
    print("es un mail")
else:
    print("no es un mail")
    
if resultado2:
    print("es un mail")
else:
    print("no es un mail")
    
#####################################33
#validar un numero de telefono

texto = "Hola Franco, mi numero de tel es  +54 1130687531"

pattern = r'\+54\s[0-9]{10}'

resultado = re.sub(pattern, "(numero oculto)", texto)

if resultado:
    print(resultado)
else:
    print("no hay telefono que ocultar")