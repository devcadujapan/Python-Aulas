"""dados = {"nome": "Josue", "idade": 25, "estado": "Sao Paulo"}
dados.update({"profissao": "dentista"})
print(dados)

# Impressao dos valores
for x in dados:
    print(dados[x])

print("------" * 12)

for x in dados.values():
    print(x)

print("------" * 12)

for x in dados.keys():
    print(x)

print("------" * 12)

for x, y in dados.items():
    print(x, y)

print("------" * 12)
"""

dados = {"nome": "Josue", "idade": 25, "estado": "Sao Paulo"}
dados.update({"profissao": "dentista"})
print(dados)

dicio = dados.copy()
print(dicio)

dicio2 = dict(dados)
print(dicio2)
