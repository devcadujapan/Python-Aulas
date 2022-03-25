# Chave : Valor
"""dicio = {"nome": "Gabriel", "ano": 1993, "valor_logico": True}
print(dicio)

dicio["nome"] = "Pedro"
print(dicio)

dicio.update({"nome": "Ana"})
print(dicio)

dicio["idade"] = 32
print(dicio)

dicio.update({"estado": "Rio de Janeiro"})
print(dicio)
"""
dados = {"nome": "Josue", "idade": 25, "estado": "Sao Paulo"}
dados.update({"profissao": "dentista"})
print(dados)

# A funcao popitem elimina o ultimo item apenas na versao 3.7 e acima
dados.popitem()
print(dados)
# Nas outras versoes, essa funcao elimina um item aleatorio

dados.pop("idade")
print(dados)

del dados["idade"]
print(dados)

dados.clear()
print(dados)
