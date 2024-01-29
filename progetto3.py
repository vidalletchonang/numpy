import pandas as pd
import matplotlib.pyplot as plt
# Visualizza l'istogramma della frequenza di abbandono del carrello
# Carica il dataset
df = pd.read_csv('Amazon Customer Behavior Survey (1).csv')

# Conteggio delle frequenze di abbandono del carrello
frequenza_abbandono_carrello = df['Cart_Abandonment_Factors'].value_counts()

# Visualizzazione dell'istogramma
plt.figure(figsize=(10, 6))
frequenza_abbandono_carrello.plot(kind='bar', color='#e74c3c', edgecolor='black', alpha=0.8)

plt.title('Frequenza di Abbandono del Carrello')
plt.xlabel('Fattori di Abbandono del Carrello')
plt.ylabel('Numero di Occorrenze')
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()

"""import pandas as pd
import matplotlib.pyplot as plt

# Carica il dataset

df = pd.read_csv('Amazon Customer Behavior Survey (1).csv')

# Trasformazione delle categorie di acquisto multiple
df['Purchase_Categories'] = df['Purchase_Categories'].str.split(';')
df_expanded = df.explode('Purchase_Categories')

# Conteggio delle frequenze delle categorie di acquisto
categorie_popolari = df_expanded['Purchase_Categories'].value_counts()

# Visualizzazione del grafico a torta delle categorie di acquisto più popolari senza percentuali
plt.figure(figsize=(10, 10))
plt.pie(categorie_popolari, labels=categorie_popolari.index, startangle=90, colors=plt.cm.Paired.colors, autopct=lambda p: f'{int(p/100*sum(categorie_popolari))} ({p:.1f}%)')

plt.title('Distribuzione delle Categorie di Acquisto')
plt.show()"""
