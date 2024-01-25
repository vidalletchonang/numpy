import pandas as pd
import numpy as np
# Leggi il file senza specificare altri parametri
df = pd.read_csv('iris.data')

# Stampa le prime cinque righe del DataFrame
print("Prime cinque righe del DataFrame:")
print(df.head())

# Stampa i nomi delle colonne
print("\nNomi delle colonne:")
print(df.columns)
