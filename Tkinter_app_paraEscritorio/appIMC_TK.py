from tkinter import*
from tkinter import messagebox

###################################
# Funciones
def calcularIMC():
    peso=int(txtPeso.get())
    altura=float(txtAltura.get())
    imc= int(peso/pow(altura,2))

    if imc < 18.5:
        messagebox.showwarning("resultado del calculo de IMC", f"El IMC calculado es de: {imc} \nsu peso es bajo")
    else:
        if imc > 18.5 and imc < 29.9:
                messagebox.showinfo("resultado del calculo de IMC", f"El IMC calculado es de: {imc} \nSu peso es Normal, ¡Felicidades!")

        else:
            messagebox.showerror("resultado del calculo de IMC", f"El IMC calculado es de: {imc} \nUsted posee sobrepeso")

###################################
#creamos la interfaz base
objVentana= Tk()

##################################
#configuracion basica de la interfaz grafica
objVentana.geometry("250x250")
objVentana.title("Aplicación para calcular IMC")



#########################################
#creamos los elementos que se van a mostrar en pantalla

#creamos el label y la caja de entrada para peso
lblPeso= Label(objVentana, text="Peso: ")
lblPeso.pack() #nos permite organizar de forma secuencial todos los elementos que vayamos agregando
txtPeso=Entry(objVentana, width= 12) #creamos un box de texto
txtPeso.pack()

#creamos el label y la caja de entrada para altura
lblAltura= Label(objVentana, text="Altura: ")
lblAltura.pack() #nos permite organizar de forma secuencial todos los elementos que vayamos agregando
txtAltura=Entry(objVentana, width= 12) #creamos un box de texto
txtAltura.pack()


btnCalcular = Button(objVentana, text="calcular IMC", command= calcularIMC)
btnCalcular.pack()





objVentana.mainloop()