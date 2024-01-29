import pandas as pd
import matplotlib.pyplot as plt

# Carica il dataset
df = pd.read_csv('Amazon Customer Behavior Survey (1).csv')

# Calcola la frequenza d'uso della feature "Save for Later"
saveforlater_counts = df['Saveforlater_Frequency'].value_counts()

# Visualizza un grafico a barre
plt.figure(figsize=(10, 6))
saveforlater_counts.plot(kind='bar', color='#9565FB', edgecolor='black', alpha=0.7)
plt.title("Frequenza d'uso della feature 'Save for Later'", color='k')
plt.xlabel('Frequenza')
plt.xticks(rotation=0, ha='right')
plt.ylabel('Conteggio')
plt.show()
