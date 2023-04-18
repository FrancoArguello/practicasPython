from tkinter import*  #de la libreria Tkinter importame todo

###########################################################################
#creamos la ventana
objVentana= Tk()


objVentana.title("Bienvenido a Safety in Life") #le colocamos un titulo a la ventana

objVentana.geometry("500x500") #tamaño inicial de ventana
###########################################################################
#le asociamos un evento al boton
#creamos las funciones
def saludar():
    lblNombre2=Label(objVentana, text="") #aca cree un nuevo label que quiero que aparezca cuando presiono el boton
    lblNombre2.grid(column=3, row =3) # aca le doy una nueva ubicacion dentro de la ventana
    lblNombre2.configure(text="hola Franco")

#btnSaludar=Button(objVentana, text="Saludar ahora", command=saludar) CON EL COMMAND ASOCIAMOS EL BOTON A LA FUNCION QUE QUEREMOS QUE REALICE

##########################################################################
#creamos objetos dentro de la ventana
btnSaludar=Button(objVentana, text="Saludar ahora", command=saludar)#creamos un boton
lblNombre= Label(objVentana, text="Franco") #creamos un label o texto plano

###########################################################################
#aca le damos una ubicacion en la ventana

lblNombre.grid(column=1, row=0) 
btnSaludar.grid(column=1, row=2)



###########################################################################
#ejecucion que nos muestra la ventana en pantalla
objVentana.mainloop() 