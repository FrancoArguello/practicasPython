#herencia simple
"""
class Estudiante(object):
    def __init__(self, edad, nombre):
        self.edad=edad
        self.nombre=nombre
class Ingenieria(Estudiante):
      
    def presentarse(self):
        print(f"soy {self.nombre} tengo {self.edad} y estudio ingenieria")


clara = Ingenieria(23, "clara Martinez")
clara.presentarse()
"""

#herencia multiple

"""
class Estudiante(object):             #Creamos la clase padre
    def __init__(self, edad, nombre): # Definimos los parámetros edad y nombre
        self.edad = edad              #Declaramos que el atributo edad es igual al argumento edad
        self.nombre = nombre          #Declaramos que el atributo nombre es igual al argumento nombre
class Instituto(object):
    def presentarinstituto (self):
        print("Estudio en el Instituto de Formación Técnica Superior N° 3")
class Ingenieria(Estudiante, Instituto): #Entre paréntesis indicamos la clase padre o principal ESTUDIANTE
                                     #Lo que la convierte a INGENIERIA en una clase hija o secundaria
    def presentarse(self):           #Creamos el método presentarse
       print (f"Soy {self.nombre} tengo {self.edad} años y estudio Ingenieria") #Se presenta llamando los atributos


Clara = Ingenieria(26, 'Clara Fraser') #Indicamos argumentos edad y nombre, creamos obj instanciando la clase Ingenieria y hereda de estudiante e instituto
Clara.presentarse()                 # Llamamos al método y Clara se presenta
Clara.presentarinstituto()

"""


#herencia con clase padre Superior
"""
class Padre(object):                 #Creamos la clase Padre
    def __init__(self, ojos, cejas): #Definimos los Atributos
        self.ojos = ojos
        self.cejas = cejas
class Hijo(Padre):                   #Creamos clase hija que hereda de Padre
    def __init__(self, ojos, cejas, cara): #creamos el constructor de la clase especificando atributos
        Padre.__init__(self, ojos, cejas) #Especificamos la clase y llamamos a su constructor + Atributos
        self.cara = cara             #Especificamos el nuevo atributo para Hijo
# usando super() quedaría:
class HijoS(Padre):                  #Creamos clase hija que hereda de Padre
    def __init__(self, ojos, cejas, cara): #creamos el constructor de la clase especificando atributos
        super().__init__(ojos, cejas)#Solicitamos a super llamar de la clase padre esos atributos
        self.cara = cara             #Especificamos el nuevo atributo para Hijo

Tomas = HijoS('Marrones', 'Negras', 'Redonda')
print("Los ojos de Tomas son ", Tomas.ojos, ", sus cejas son ", Tomas.cejas, " y su cara ", Tomas.cara)

"""
# Herencia Multiple y Atributos no sirve Super(), hay que usar los constructores
"""
# de las clases especificándolas por su nombre. Y si cambiamos el nombre u orden de
# la clase debemos especificarlo.
class Padre(object):                 #Creamos la clase Padre
    def __init__(self, ojos, cejas): #Definimos los Atributos
        self.ojos = ojos
        self.cejas = cejas
class Madre(object):                 #Creamos la clase Padre llamada Madre
    def __init__(self, brazos, piernas): #Definimos los Atributos
        self.brazos = brazos
        self.piernas = piernas
class Hijo(Padre, Madre):            #Creamos clase hija que hereda de Padre y luego de Madre
    def __init__(self, ojos, cejas, cara, brazos, piernas): #creamos el constructor de la clase especificando atributos
        Madre.__init__(self, brazos, piernas)
        Padre.__init__(self, ojos, cejas)#Solicitamos a super llamar de la clase padre esos atributos
        self.cara = cara

Tomas = Hijo('Marrones', 'Negras', 'Redonda', 2, 2)
print(Tomas.ojos, Tomas.cejas, Tomas.cara, Tomas.piernas, Tomas.brazos)
print("Los ojos de Tomas son ", Tomas.ojos, ", sus cejas son ", Tomas.cejas, " y su cara ", Tomas.cara, ", tiene ", Tomas.piernas, " piernas y ", Tomas.brazos, " brazos.")
"""

# - Declaramos Variables de Clase 
"""
class Perros(object):
    'Clase para los perros'           #Descripción
    Collar = True                     #Variable de clase Estática
    def __init__(self, salud, hambre):
        self.salud = salud            #Variable de Instancia
        self.hambre = hambre          #Variable de Instancia
print("El perro tiene collar: ", Perros.Collar) #podemos accederla sin crear un objeto(sin instanciar)
"""
# Accedemos a variables de Instancia 

# print (Perros.hambre) #-> ASI NO PODES!, porque hambre es una variable de instancia
#Debes instanciar:
Pequines = Perros(100, 5)
print("¿Cuanto kilos come un Pequines?: ", Pequines.hambre)



