import pandas as pd

# Carica il dataset
df = pd.read_csv('wine.csv')

# Calcolare la numerosità
numerisita = df.count()

# Calcolare la media
media = df.mean()

# Calcolare la mediana
mediana = df.median()

# Calcolare la moda
moda = df.mode().iloc[0]

# Calcolare i quartili
quartili = df.quantile([0.25, 0.5, 0.75])


# Puoi anche combinare tutte queste statistiche in un unico DataFrame
statistiche_base = pd.DataFrame({
    'Numerosita': numerisita,
    'Media': media,
    'Mediana': mediana,
    'Moda': moda,
    'Primo Quartile': quartili.loc[0.25],
    'Mediana (Quartile 2)': quartili.loc[0.5],
    'Terzo Quartile': quartili.loc[0.75],
})

print(statistiche_base)
