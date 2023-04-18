

nombre = "Jose"
print(nombre)
nombre = str("jose")
print(nombre)

nombre, apellido = "Martin", "Quintana"
print(nombre)
print(apellido)

numero = 1.4

datos_en_tupla = ("Franco", "arguello", 29)
datos_en_lista = ["Franco", "arguello", 29]

nombre, apellido, edad = datos_en_tupla
print(
    f'el nombre es: {nombre}, el apellido es: {apellido} y su edad es: {edad}')


nombre, apellido, edad = datos_en_lista
print(
    f'el nombre es: {nombre}, el apellido es: {apellido} y su edad es: {edad}')


# esto mismo se puede haceer en set(conjuto de datos) pero esta limitado ya que no deja desempaquetar numeros, solo str


"""tipos de datos
int
str
float
bool
list
tuple
dict
set
obj

"""
print(type(numero))
