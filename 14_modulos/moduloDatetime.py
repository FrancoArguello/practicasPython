import datetime #para trabajar con fechas
from datetime import timedelta
from time import sleep #para trabajar con tiempo de espera de ejecucion

tiempo = datetime.datetime.now()
dia_hora = datetime.datetime.now()
print(dia_hora)

#formato de fecha año, mes, dia
print(tiempo.strftime("%Y, %m, %d"))

print(tiempo.strftime("%d, %m, %Y"))

sleep(4) #esto indica que la app va a estar en pausa 4 segundos y ahi vuelve a seguir con todo el proceso que continue