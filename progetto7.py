from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd  # Aggiungi questa riga per importare il modulo pandas
# Esplora le risposte dei clienti per identificare le aree di miglioramento segnalate
# Carica il dataset
dataset = pd.read_csv('Amazon Customer Behavior Survey (1).csv')

# Seleziona le colonne contenenti le risposte dei clienti
risposte_clienti = dataset['Improvement_Areas'].dropna()

# Unisce tutte le risposte in un'unica stringa
testo_completo = ' '.join(risposte_clienti)

# Crea una nuvola di parole
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(testo_completo)

# Visualizzazione della nuvola di parole
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Nuvola di Parole delle Aree di Miglioramento Segnalate')
plt.show()

