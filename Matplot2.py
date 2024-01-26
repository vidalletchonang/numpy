import pandas as pd
import matplotlib.pyplot as plt
import urllib.request

url = "https://raw.githubusercontent.com/plotly/datasets/master/stockdata.csv"
filename = "stockdata.csv"

# Scarica il file CSV
urllib.request.urlretrieve(url, filename)

# Carica il dataset usando pandas
df = pd.read_csv(filename)

# Estrai le prime 20 istanze della colonna AAPL
aapl_data = df["AAPL"].head(20)

# Configura il grafico secondo le specifiche richieste
plt.figure(figsize=(10, 5))
plt.plot(df["Date"].head(20), aapl_data, color='red', linestyle='--', marker='o', markerfacecolor='black', linewidth=2)

# Aggiungi titoli e etichette degli assi
plt.title('Azioni Apple')
plt.xlabel('Data')
plt.ylabel('Valore')

# Aggiungi la rotazione alle etichette dell'asse x
plt.xticks(rotation=45)

# Mostra il grafico
plt.show()

"""import pandas as pd
import matplotlib.pyplot as plt
import urllib.request

url = "https://raw.githubusercontent.com/plotly/datasets/master/stockdata.csv"
filename = "stockdata.csv"

# Scarica il file CSV
urllib.request.urlretrieve(url, filename)

# Carica il dataset usando pandas
df = pd.read_csv(filename)

# Estrai le prime 20 istanze della colonna AAPL
aapl_data = df["AAPL"].head(20)

# Configura il grafico secondo le specifiche richieste
plt.figure(figsize=(10, 5))
plt.plot(df["Date"].head(20), aapl_data, color='red', linestyle='--', marker='o', markerfacecolor='black', linewidth=2)

# Aggiungi titoli e etichette degli assi
plt.title('Azioni Apple')
plt.xlabel('Data')
plt.ylabel('Valore')

# Aggiungi la rotazione alle etichette dell'asse x
plt.xticks(rotation=45)

# Mostra il grafico
plt.show()"""

