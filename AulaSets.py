"""sets: Coleção não ordenada imutável e que não permite valores duplicados"""
# Os sets tambem sao conhecidos como conjuntos e não sefue uma ordem

"""conjunto = {"item", 3, True, 4.7, "sao paulo"}
print(type(conjunto))
print(conjunto)
print(len(conjunto))"""

# Construtores: (tuple, list, dict, set)
# Transformando uma tupla em set

"""tupla = (3, 7, 9, 5)
conjunto = set(tupla)
print(conjunto)"""

# Outra maneira mais simple de transformar tupla em set

"""conjunto = set((3, 7, 9, 5))
print(conjunto)

conj = {"item1", "item2", "item3", "item4", "item5"}

for x in conj:
    print(x)"""

conjunto = {4, 6, 8, 9, 1}
print(6 in conjunto)
print(12 in conjunto)
