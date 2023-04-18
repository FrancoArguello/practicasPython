from tkinter import*

objVentana=Tk()
objVentana.title("Aplicación con Python")
objVentana.geometry("500x500")

#creamos un label para mostrar el nombre
lblNombre= Label(objVentana, text="...")
lblNombre.grid(column=0, row= 0)

#creamos un campo para escribir nuestro nombre
txtNombre= Entry(objVentana, width=12)
txtNombre.grid(column=1, row=0)


#creamos una funcion para pedir un dato de entrada y asociarlo al txtNombre

def accionSaludar():
    datoEntrada = txtNombre.get()
    lblNombre.configure(text=datoEntrada)

#creamos un boton para usar la funcion
btnNombre = Button(objVentana, text="presiona este bóton", command=accionSaludar)
btnNombre.grid(column=2, row=2)

#funcion para abrir la ventana
objVentana.mainloop()

