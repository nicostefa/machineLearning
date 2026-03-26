import numpy as np


vector = np.array([1, 2, 3])
print(vector, type(vector))

# Maschera booleana
mask = vector > 2
print(mask)

vector2 = vector[mask]
print(vector2)

# Operazioni sui vettori
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = a + b
print(c)

# prodotto scalare
dot_product = np.dot(a, b)
print(dot_product)

# operazioni su singolo vettore
v = np.array([5, 8, 0, 9, 2])
v = np.sort(v)
print(v)
np.random.shuffle(v)
print(v)

# Funzioni