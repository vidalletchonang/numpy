import pandas as pd
import matplotlib.pyplot as plt
# Esplorazione delle recensioni:  Esamina la frequenza con cui i clienti lasciano recensioni
df = pd.read_csv('Amazon Customer Behavior Survey (1).csv')
# Conteggio delle frequenze delle recensioni
frequenza_recensioni = df['Review_Left'].value_counts()

# Visualizzazione dell'istogramma delle frequenze delle recensioni
plt.figure(figsize=(8, 6))
frequenza_recensioni.plot(kind='bar', color='#3498db', edgecolor='black', alpha=0.8)

plt.title('Frequenza delle Recensioni dei Clienti')
plt.xlabel('Recensioni Lasciate')
plt.ylabel('Numero di Clienti')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()