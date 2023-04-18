#instalamos el metplotlib con py -m pip install matplotlib en el cmd como admin
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("graficos\\pedos.csv", encoding= "UTF-8")

sns.lineplot(x="fecha", y="terremotos", data= df) #le pasamos el parametro del eje X e Y y con data de donde tiene que sacar esos valores

plt.plot("01-07",22,"o") #colocamos un punto en el dia que mas terremotos secedieron

plt.show() #con el show mostramos el grafico
