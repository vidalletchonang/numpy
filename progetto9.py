import pandas as pd
import matplotlib.pyplot as plt
# Importanza delle Recensioni dei Clienti
# Carica il dataset
df = pd.read_csv('Amazon Customer Behavior Survey (1).csv')

# Esamina la distribuzione di Customer_Reviews_Importance
importance_counts = df['Customer_Reviews_Importance'].value_counts()

# Visualizza un grafico a barre
plt.figure(figsize=(10, 6))
importance_counts.plot(kind='bar', color='skyblue')
plt.title('Importanza delle Recensioni dei Clienti')
plt.xlabel('Livello di Importanza')
plt.ylabel('Frequenza ')
plt.xticks(rotation=45)
plt.show()
