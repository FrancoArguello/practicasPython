from tkinter import *
from tkinter import messagebox


objVentana = Tk()

objVentana.geometry("500x500")
objVentana.title("Hola Mundo")


def mostrarMensaje():
    # nos muestra una especie de ventanita emergente
    messagebox.showinfo("esto es un mensaje",
                        "saludos, esta app es una muestra")
    # el primer texto es el titulo de la ventanita, el segundo es el contenido del mensaje a mostrar
    # nos muestra una ventana con el logo de advertencia o peligro
    messagebox.showwarning("esto es un mensaje", "peligro")
    # nos muestra una venta con el logo de error
    messagebox.showerror("esto es un mensaje", "error")

    # preguntar y guardar valor de respuesta
    # nos sirve para preguntar y obtener una respuesta yes/no y guardamos el valor ne la variable
    respuesta = messagebox.askquestion("titulo", "queres seguir en la app")
    # nos sirve para ver si se capturo bien la respuesta del usuario
    messagebox.showinfo("esto es un mensaje", "presionaste: " + str(respuesta))


btnMensaje = Button(objVentana, text="mostar mensaje", command=mostrarMensaje)
btnMensaje.grid(column=0, row=0)


objVentana.mainloop()
