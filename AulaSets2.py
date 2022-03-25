# Adicionando Elementos
"""set1 = {"item1", "item2", "item3"}
print(set1)
set1.add("item5")
print(set1)
set1.add(8)
set1.add(True)
print(set1)"""

"""set1 = {4, 5, 7, 8, 1}
set2 = {"item3", "item5", "item1"}
set1.update(set2)
print(set1)

# Simplificando o codigo acima

set1 = {4, 5, 7, 8, 1}
set1.update({"item3", "item5", "item1"})
print(set1)"""
# Podemos passar uma tupla e uma lista para o set
"""set1 = {4, 5, 7, 8, 1}
set1.update([1, 4, 7, 8, 9, 3])
print(set1)"""

# Removendo Elementos ( pop , remove, discard, del, clear)

set1 = {1, 3, 4, 5, "item5", 7, 8, 9, "item6"}
print(set1)

# Remove o ultimo elemento, mas no conjunto pode ser qualquer um
set1.pop()
print(set1)

# Remove o elemento escolhido
set1.remove("item5")
print(set1)

# se tentar remover um elemento que não está no conjunto, não tem mensagem de erro
set1.discard("item6")
print(set1)

# Com o clear ele deixa o set1 vazio
set1 = {1, 3, 4, 5, "item5", 7, 8, 9, "item6"}
set1.clear()
print(set1)

# del exclue todo conjunto e da erro quando pede pra imprimir
del set1
print(set1)
