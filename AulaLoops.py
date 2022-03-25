# Concatenacao de Tuplas
tupla = ("iten1",)
tupla2 = ("a", "b")
tupla = tupla + tupla2
print(tupla)

tupla = tupla * 3
print(tupla)

tupla = "item1", "item2", "item3"
print(tupla)

for variavel in tupla:
    print(variavel)

for x in range(len(tupla)):
    print(x, tupla[x])

(x, y, z) = tupla
print("x: ", x)
print("y: ", y)
print("z: ", z)
# Para nao dar erro, tem que imprimir todos os elementos

(x, *y) = tupla
print("x: ", x)
print("y: ", y)

# Desempacotando uma lista ou tupla
tupla = (1, 2, 3, 4, 5, 6)
print(tupla)
(x, *y, z) = tupla
print("x: ", x)
print("y: ", y)
print("z: ", z)
