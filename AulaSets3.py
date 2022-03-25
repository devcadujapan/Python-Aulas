"""conjunto1 = {1, 5, 8, 9}
conjunto2 = {3, 6, 2}

conjunto3 = conjunto1.union(conjunto2)
print(conjunto3)"""

# Imprime somente os elementos que se repete entre os dois conjuntos
"""conjunto1 = {1, 5, 3, 2}
conjunto2 = {3, 6, 2}

conjunto3 = conjunto1.intersection(conjunto2)
print(conjunto3)"""

"""conjunto1 = {1, 5, 3, 2}
conjunto2 = {3, 6, 2}

conjunto1.intersection_update(conjunto2)
print(conjunto1)"""

# Impressao dos elementos que sao unicos nos dois conjuntos
conjunto1 = {1, 5, 3, 2}
conjunto2 = {3, 6, 2}

conjunto1.symmetric_difference(conjunto2)
print(conjunto1)

conjunto1 = {1, 5, 3, 2}
conjunto2 = {3, 6, 2}
conjunto1.symmetric_difference_update(conjunto2)
print(conjunto1)
