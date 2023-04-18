#declaramos la clase
class calcularIMC:
    def __init__(self, peso, estatura): #constructor encargado de inicializar cuando se crea una instancia
        self.peso=peso
        self.estatura=estatura
    
    def imprimirIMC(self):
        self.imc=self.peso/pow(self.estatura,2)
        print(f"el IMC es: {self.imc}")
    
#herencia simple -> acá podemos usar las funciones de la clase padre pero no las padres las funciones de las class hijas
class mostrarPeso(calcularIMC):
    def imprimirPeso(self):
        if self.imc < 18.5:
            print(f"su peso es bajo")
        else:
            if self.imc > 18.5 and self.imc < 29.9:
                print(f"su peso es normal")
            else:
                print("usted posee obesidad")

#instanciar la clase

#objeto 1
objCalcularIMC = mostrarPeso(130,1.79)
objCalcularIMC.imprimirIMC() # usa una funcion de la clase padre
objCalcularIMC.imprimirPeso() # usa una funcion de la clase hija