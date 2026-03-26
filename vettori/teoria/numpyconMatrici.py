import numpy as np


matrix = np.array([[1, 2, 3,23], [4, 5, 6, 23], [7,8,9,23]])
print(matrix, type(matrix))
print(matrix.shape)
print(matrix.size)

# Ridimensionamento - il reshape crea sempre una matrice
reshaped_matrix = matrix.reshape(4, 3)
print(reshaped_matrix, reshaped_matrix.shape)

# Trasportazione in vettore flattening - se si usasse rehape(12) si otterrebbe una matrice, con flatten invece si ottiene un vettore
flattened_matrix = matrix.flatten()
print(flattened_matrix, flattened_matrix.shape)


# Broadcasting - operazioni tra matrici di dimensioni diverse
# La somma si può fare anche su matrici di dimensioni diverse, purché siano compatibili. In questo caso, la matrice 2 viene "broadcastata" per adattarsi alla matrice 1, e l'operazione di somma viene eseguita elemento per elemento.
print("\nBroadcasting")
mattrx_1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_2 = np.array([1, 2, 3])
result = mattrx_1 + matrix_2
print(result)

# Prodotto matrice-matrice - scalare. Il prodotto può essere eseguito solo se il numero di colonne della prima matrice è uguale al numero di righe della seconda matrice. Il risultato è una nuova matrice in cui ogni elemento è calcolato come la somma dei prodotti degli elementi corrispondenti delle righe della prima matrice e delle colonne della seconda matrice.
# Il risultato sarà una nuova matrice di dimensioni (m, p), dove m è il numero di righe della prima matrice e p è il numero di colonne della seconda matrice.
print("\nProdotto matrice-matrice - scalare")
matrix_a = np.array([[1, 2, 3], [4, 5, 6]])
matrix_b = np.array([[7, 8], [9, 10], [11, 12]])
product = np.dot(matrix_a, matrix_b)
print(product)

# Generazione Matrici e vettori
print("\nGenerazione Matrici e vettori")
matrix_zeros = np.zeros((3, 4))
print("matrix_zeros:", matrix_zeros)

matrix_eye = np.eye(4)
print("matrix_eye:", matrix_eye)

matrix_random = np.random.random((3, 4))
print("matrix_random:", matrix_random)


