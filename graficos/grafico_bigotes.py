#instalamos el metplotlib con py -m pip install matplotlib en el cmd como admin
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("graficos\\bigotes.csv", encoding= "UTF-8")

sns.boxplot(x="categoria", y="valor", data= df) #le pasamos el parametro del eje X e Y y con data de donde tiene que sacar esos valores


plt.show() #con el show mostramos el grafico
