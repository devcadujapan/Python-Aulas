# O Argumento Arbitario *args - Essa funcao recebe argumentos que serao atrubuidos em uma tupla
"""
def imprimir_imovel(nomeImovel, n_quartos, vagasGaragem=None, *args):
    print("---------------------")
    print("Titulo: ", nomeImovel)
    print("Quartos: ", n_quartos)
    if vagasGaragem != None:
        print("Vagas na garagem: ", vagasGaragem)


imprimir_imovel("Loja Comercial", 2, 5, "desconto")
"""

"""
def imprimir_nomes(*nomes):
    print(nomes)


imprimir_nomes("Ana", "Beto", "Claudio", "Fernanda", "Marcelo")
print("---------------------")
lista = ["Ana", "Beto", "Claudio", "Fernanda", "Marcelo"]
imprimir_nomes(*lista)
"""


# Argumento Arbitario **Kwargs - Keyword Arguments
# Essa funcao recebe argumentos que serao atribuidos em um dicionario

def imprimir_nomes(**nomes):
    print(nomes)


imprimir_nomes(nome="Ana", sobrenome="Figueira")
print("-------------------")


def imprimir_nomeTodo(**nomes):
    print(f"{nomes['nome']} {nomes['sobrenome']}")


imprimir_nomeTodo(nome="Jair", sobrenome="Mendes")
