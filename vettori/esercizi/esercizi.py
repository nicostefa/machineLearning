""" 
    Esercizio 1: 
    Acquisici in input una lista di numeri, definisci una funzione per creare un'array numpy di Float partendo dalla lista 
    con l'ordine dei numeri invertito.
"""

import numpy as np

list_in = input("inserisci lista numerica: ").strip().split()
vec = np.array(list_in, float)
print(vec[::-1])


"""
    Esercizio 2:
    Shape e Reshape: Acquisisci in inpu una lista di 9 numeri interi, converti tale lista in un array numpy di
    dimensione 3x3
"""

list_in = input("inserisci 9 numeri interi: ").strip().split()
vect = np.array(list_in, int)
matr = vect.reshape(3,3)
print(matr)

"""
    Esercizio 4:
    4. Aritmetica degli array

        - Acquisisci due numeri N e M in input
        - Acquisisci N righe di interi e utilizzale per creare la matrice numpy A
        - Acquisisci N righe di interi e utilizzale per creare la matrice numpy B
        - Stampa la somma delle matrici A e B
        - Stampa la differenza delle matrici A e B
        - Stampa il prodotto delle matrici A e B
        - Stampa la divisione tra interi tra le matrici A e B
        - Stampa il risultato del modulo tra le matrici A e B
        - Stampa il risultato della matrice A elevata la matrice B.
"""
print("\nEsercizio 4")
N, M = map(int, input().strip().split())
matrix_a = np.array([input().strip().split() for _ in range(N)], int)
matrix_b = np.array([input().strip().split() for _ in range(N)], int)

print(matrix_a + matrix_b)