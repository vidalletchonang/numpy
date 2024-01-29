import pandas as pd
import matplotlib.pyplot as plt
# Visualizza la distribuzione della frequenza di acquisto per capire quanto spesso i clienti effettuano acquisti, per analisi della frequenza di acquisto
# Carica il dataset
df = pd.read_csv('Amazon Customer Behavior Survey (1).csv')

# Split delle categorie di acquisto multiple e creazione di nuove righe
df['Purchase_Categories'] = df['Purchase_Categories'].str.split(';')
df_expanded = df.explode('Purchase_Categories')

# Conta le frequenze delle categorie di acquisto
categorie_popolari = df_expanded['Purchase_Categories'].value_counts()

# Visualizza le categorie di acquisto più popolari
plt.figure(figsize=(12, 8))
categorie_popolari.plot(kind='bar', color='#3498db', edgecolor='black', alpha=0.8)

plt.title('Categorie di Acquisto più Popolari')
plt.xlabel('Categorie di Acquisto')
plt.ylabel('Numero di Acquisti')
plt.xticks(rotation=45, ha='right')  # Ruota le etichette sull'asse x per una migliore leggibilità
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()

