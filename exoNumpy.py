import numpy as np

# Lista di liste originale
mat = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14]]

# Trasforma la lista di liste in un array NumPy
mat = np.array(mat)

# Accesso ai singoli elementi
elemento = mat[1, 2]  # Elemento nella seconda riga e terza colonna
print(elemento)

