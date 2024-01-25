import pandas as pd

# Definisci i nomi delle colonne dal file .names
column_names = [
    "sepal_length", "sepal_width", "petal_length", "petal_width", "class"
]

# Leggi il file specificando i nomi delle colonne
df = pd.read_csv('iris.data', header=None, names=column_names)

# Stampiamo le prime cinque righe
print("Prime cinque righe del DataFrame:")
print(df.head())

# Stampiamo le ultime dieci righe
print("\nUltime dieci righe del DataFrame:")
print(df.tail(10))

# Stampiamo un riepilogo dei descrittori statistici del dataset
print("\nRiepilogo dei descrittori statistici:")
print(df.describe())
