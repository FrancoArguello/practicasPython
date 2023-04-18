edad = 20

if edad > 18:
    mensaje= "es mayor"
elif edad == 17:
    mensaje = "casi que sos mayor"
else:
    mensaje = "sos menor"    
print(mensaje)


######################################
#Operadores Ternarios

mensaje ="es mayor" if edad > 18 else "es menor"
print(mensaje)