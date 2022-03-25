# Index     0        1       2
lista = ["carro", "barco", "aviao"]
print(lista)

for x in range(len(lista)):
    print(x, lista[x])

# remove ultimo elemento
#lista.pop()
# Remove elementos especificos
#lista.remove("barco")
#lista.pop(0)
#del lista[0]

# Limpando a Lista
carrinho_de_compras = ["pao", "carne", "verdura", "alface"]
#carrinho_de_compras.clear()
print(carrinho_de_compras)

# Colocar em ordem alfabetica
carrinho_de_compras.sort()

# colocar em ordem Decrescente
lista2 = [6, 57, 21, 4, 90, 1, 45, 33]
print(lista2)
lista2.sort(reverse=True)
print(lista2)

# Coloca em ordem alfabetica mesmo com minuscula mesclada
lista3 = ["Joao", "Fabiana", "suzane", "Ana", "beatriz", "zenilda"]
print(lista3)
lista3.sort()
print(lista3)
lista3.sort(key=str.lower)
print(lista3)
