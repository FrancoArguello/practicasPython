#instalamos el metplotlib con py -m pip install matplotlib en el cmd como admin
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("graficos\\inversiones.csv", encoding= "UTF-8")

sns.barplot(x="fuente", y="ingresos", data= df) #le pasamos el parametro del eje X e Y y con data de donde tiene que sacar esos valores

#mostrando el total de ingresos
total_ingresos = df.sum()
print(f"El total de ingresos es de: {total_ingresos} dolares") #nos muestra en consola

plt.show() #con el show mostramos el grafico
