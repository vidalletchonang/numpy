import pandas as pd
import matplotlib.pyplot as plt
import urllib.request

url = "https://raw.githubusercontent.com/plotly/datasets/master/stockdata.csv"
filename = "stockdata.csv"

# Scarica il file CSV
urllib.request.urlretrieve(url, filename)

# Carica il dataset usando pandas
df = pd.read_csv(filename)

# Estrai i dati relativi a MSFT
msft_data = df["MSFT"]

# Plot per l'andamento di MSFT
plt.figure(figsize=(10, 5))
plt.plot(df["Date"], msft_data, marker='o')
plt.title('Andamento MSFT')
plt.xlabel('Data')
plt.ylabel('Valore MSFT')
plt.xticks(rotation=45)
plt.show()

# Estrai le prime 5 righe
first_five = df.head(5)

# Plot per le prime 5 righe
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.plot(first_five["Date"], first_five["MSFT"], marker='o')
plt.title('Primi 5 giorni - Andamento MSFT')
plt.xlabel('Data')
plt.ylabel('Valore MSFT')
plt.xticks(rotation=45)

# Estrai le ultime 5 righe
last_five = df.tail(5)

# Plot per le ultime 5 righe
plt.subplot(1, 2, 2)
plt.plot(last_five["Date"], last_five["MSFT"], marker='o')
plt.title('Ultimi 5 giorni - Andamento MSFT')
plt.xlabel('Data')
plt.ylabel('Valore MSFT')
plt.xticks(rotation=45)

# Mostra il grafico
plt.tight_layout()
plt.show()


"""import matplotlib.pyplot as plt
# Dati del dataset
data = {
    "MSFT": [23.950705, 23.910599, 23.774242, 24.006852, 24.030914, 23.790284],
    "Date": ["2007-01-03", "2007-01-04", "2007-01-05", "2007-01-08", "2007-01-09", "2007-01-10"]
}

# Estraiamo i primi 5 e ultimi 5 dati della colonna MSFT e Date
first_five_dates = data["Date"][:5]
first_five_msft = data["MSFT"][:5]

last_five_dates = data["Date"][-5:]
last_five_msft = data["MSFT"][-5:]

# Plot per i primi 5 dati
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.plot(first_five_dates, first_five_msft, marker='o')
plt.title('Primi 5 giorni - Andamento MSFT')
plt.xlabel('Data')
plt.ylabel('Valore MSFT')

# Plot per gli ultimi 5 dati
plt.subplot(1, 2, 2)
plt.plot(last_five_dates, last_five_msft, marker='o')
plt.title('Ultimi 5 giorni - Andamento MSFT')
plt.xlabel('Data')
plt.ylabel('Valore MSFT')

# Mostra il grafico
plt.tight_layout()
plt.show()"""



