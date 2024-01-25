import numpy as np

# Creare il ndarray 5x5
matrice_originale = np.array([
    [10, 22, 21, 8, 9],
    [9, 42, 3, 18, 11],
    [5, 4, 30, 12, 29],
    [37, 31, 7, 2, 26],
    [8, 6, 4, 33, 15]
])

# Calcolare il minimo e il massimo
minimo_valore = np.min(matrice_originale)
massimo_valore = np.max(matrice_originale)

# Sottrarre il minimo da ogni elemento e dividere per la differenza tra massimo e minimo
matrice_normalizzata = (matrice_originale - minimo_valore) / (massimo_valore - minimo_valore)

print("Matrice Normalizzata:")
print(matrice_normalizzata)
