import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
# Utilizza una matrice di correlazione o scatter plot per esaminare le relazioni tra le diverse variabili nel dataset
# Carica il dataset
dataset = pd.read_csv('Amazon Customer Behavior Survey (1).csv')

# Seleziona solo le colonne numeriche
colonne_numeriche = dataset.select_dtypes(include='number').columns

# Calcola la matrice di correlazione solo per le colonne numeriche
corr_matrix = dataset[colonne_numeriche].corr()

# Crea un heatmap della matrice di correlazione
plt.figure(figsize=(12, 10))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=.5)
plt.title('Matrice di Correlazione tra Variabili Numeriche')
plt.xticks(rotation=45)
plt.show()

# Oppure, puoi visualizzare scatter plot tra coppie di variabili numeriche
""" sns.pairplot(dataset[colonne_numeriche])
plt.suptitle('Scatter Plot tra Variabili Numeriche', y=1.02)
plt.show()"""



