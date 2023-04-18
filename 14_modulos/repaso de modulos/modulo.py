import moduloSaludar as saludar #importamos el modulo  y con el as le cambiamos el nombre al modulo
from moduloSaludar import saludar_raro #as raro --- tambien asi le podemos cambiar el nombre a la funcion


saludo= saludar.saludar("Franco") #aca necesitamos poner el nombre del modulo xq lo importamos completo
saludo_raro= saludar_raro("Jorge") #aca no necitamos poner el nombre del modulo ya que solo importamos la funcion

#para ver las propiedades y metodos de el namespace
print(dir(saludar))

#para acceder al nombre del modulo en el que nos encontramos
print(__name__)

#para acceder al nombre del modulo llamado
print(saludar.__name__)


###################################################
# ENRRUTAMIENTO DE MODULOS DE OTRAS CARPETAS
#SUPONGAMOS QUE TENEMOS EL MODULO "TITANES" EN LA CARPETA "MITOLOGIA" y esta en la misma ruta en la que estamos trabajando

#IMPORT mitologia.titanes --> aca ponemos primero el nombre de la carpera y luego el nombre del modulo
# con el as se puede cambiar el nombre tambien


#AHORA SI LA CARPETA ESTA UBICADA EN UNA CAPA ANTERIOR O MAS SE IMPORTA ASI
import sys 

print(sys.path) #con esto veo en que ruta estoy
sys.path.append('d:\\ESTUDIOS\\TEC-SUP-DESARROLLO-DE-SOFTWARE\\python\\ejercicios') #aca agregro la ruta a nuestro path

import ejercicio1  #aca nos va a marcar un warning pero no es nada, funciona perfectamente
print(ejercicio1.obtener_compañeros) #asi invocamos a la funcion que necesitamos de este modulo


from ejercicio1 import obtener_compañeros as funcion #aca del modulo ejercicio1 importamos la funcion que queremos y le cambiamos el nombre para ser mas comodo su uso
print(funcion)