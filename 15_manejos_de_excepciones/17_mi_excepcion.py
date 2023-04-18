#las clases por pep8 se deben escribir en CamelCase() y con la primera letra en mayuscula

#aca creamos mi excepcion personalizada
class MiExcepcion(Exception):
    def __init__(self,error):
        print(f"impresionante cometiste el siguiente error: {error}")
        
        
#raise es la palabra clave para decirle al sistema que debe lanzar la excepcion que le ordenamos

#raise ZeroDivisionError("que boludo dividiste por cero") #de esta manera lanzamos una excepcion y con un msj directamente 
#aca lanzamos directamente nuestra excepcion
#raise MiExcepcion(f"Error {23}")


#aca manejamos NUESTRA PROPIA EXCEPCION con el try
try:
    raise MiExcepcion("salameeee") #lo que le paso por parametro es el valor que me va a mostrar en el print de la funcion
except:
    print("como vas a cometer ese error")