import numpy as np

lunghezza_struttura = 28.75  # Lunghezza della struttura in cm
numero_rivetti = 15         # Numero totale di rivetti

# Calcolare la distanza tra i rivetti (ignorando il primo e l'ultimo)
distanza_tra_rivetti = lunghezza_struttura / (numero_rivetti - 1)

# Creare un array NumPy di posizioni dei rivetti
posizioni_rivetti = np.arange(0, lunghezza_struttura + distanza_tra_rivetti, distanza_tra_rivetti)

# Visualizzare le posizioni dei rivetti
print("Posizioni dei rivetti:")
print(posizioni_rivetti)
