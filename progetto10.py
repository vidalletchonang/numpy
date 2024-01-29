import pandas as pd
import matplotlib.pyplot as plt

# Carica il dataset
df = pd.read_csv('Amazon Customer Behavior Survey (1).csv')

# Calcola il conteggio della distribuzione del metodo di ricerca dei prodotti
Product_Search_Method_counts = df['Product_Search_Method'].value_counts()

# Visualizza il grafico a barre
plt.bar(Product_Search_Method_counts.index, Product_Search_Method_counts.values, color='green')
plt.title('Amazon Customers Method')
plt.xlabel('Method')
plt.ylabel('Number of Customers')
plt.show()
