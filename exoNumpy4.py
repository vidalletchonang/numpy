import numpy as np

# Inizializzare un array vuoto delle stesse dimensioni della matrice
ndarray_copiato = np.empty((3, 4))

# Inserire i valori nelle posizioni adatte
ndarray_copiato[0] = [1, 1, 1, 1]
ndarray_copiato[1] = [5, 1, 1, 1]
ndarray_copiato[2] = [20, -4, 0, 42]

print("Approccio 1 - ndarray copiato:")
print(ndarray_copiato)

import numpy as np

# Creare una lista di liste con gli stessi valori della matrice
lista_di_liste = [[1, 1, 1, 1],
                  [5, 1, 1, 1],
                  [20, -4, 0, 42]]

# Effettuare un casting della lista di liste a ndarray
ndarray_copiato = np.array(lista_di_liste)

print("Approccio 2 - ndarray copiato:")
print(ndarray_copiato)
