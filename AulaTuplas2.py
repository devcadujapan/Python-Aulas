# Modificando uma Tupla Atraves da substitucao da variavel

tupla = ("item1", "item2")
print(tupla)

tupla = ("item3", "item4", "verde")
print(tupla)

tupla = (2, 4.6, True, "Mala")
print(tupla)

# Deixa de ser tupla e se torna uma variavel String
tupla = ("produto")
print(tupla)
print(type(tupla))
# Tupla de 1 elemento
tupla = ("produto",)
print(tupla)
print(type(tupla))
# sem parenteses
tupla = "produto", "produto2", "produto3"
print(tupla)
print(type(tupla))

print(">>>>>>>" * 10)

# Transforma Tupla em Lista
tupla = ("item1", "item2", "item3", "item4")
lista = list(tupla)
print(tupla)
print(lista)

lista.append("item5")
print(lista)

# Transformando uma Lista em uma Tupla
tupla = tuple(lista)
print(tupla)
