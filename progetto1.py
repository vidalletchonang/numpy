import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Amazon Customer Behavior Survey (1).csv')
# Trasformazione delle categorie di acquisto multiple
df['Purchase_Categories'] = df['Purchase_Categories'].str.split(';')
df_expanded = df.explode('Purchase_Categories')

# Conteggio delle frequenze delle categorie di acquisto
categorie_popolari = df_expanded['Purchase_Categories'].value_counts()

# Visualizzazione del grafico a torta delle categorie di acquisto più popolari
plt.figure(figsize=(10, 10))
plt.pie(categorie_popolari, labels=categorie_popolari.index, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)

plt.title('Distribuzione Percentuale delle Categorie di Acquisto')
plt.show()