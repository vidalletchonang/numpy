import numpy as np

linear_data = np.array([x for x in range(27)])
reshaped_data = linear_data.reshape((3, 3, 3))

# Numero di dimensioni dell'array reshaped_data
numero_di_dimensioni = reshaped_data.ndim
print("Numero di dimensioni:", numero_di_dimensioni)