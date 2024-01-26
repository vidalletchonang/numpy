import pandas as pd
import matplotlib.pyplot as plt
import urllib.request

url = "https://raw.githubusercontent.com/plotly/datasets/master/stockdata.csv"
filename = "stockdata.csv"

# Scarica il file CSV
urllib.request.urlretrieve(url, filename)

# Carica il dataset usando pandas
df = pd.read_csv(filename)

# Converti la colonna 'Date' in tipo datetime
df['Date'] = pd.to_datetime(df['Date'])

# Imposta la colonna 'Date' come indice del DataFrame
df.set_index('Date', inplace=True)

# Visualizza l'andamento di tutte le azioni sullo stesso grafico
df.plot(figsize=(12, 6), title='Andamento Azioni', xlabel='Data', ylabel='Valore')

# Sposta la legenda in basso a destra
plt.legend(loc='lower right')

# Mostra il grafico
plt.show()
