# Parametro Padrao - Define argumentos nao  obrigatorios
"""def imprimir_nome(nome="nome", sobrenome="sobrenome", idade="idade"):
    print("Nome: ", nome)
    print("Sobrenome: ", sobrenome)
    print("Idade: ", idade)
    print("-------------------------")


imprimir_nome()
imprimir_nome("Marcelo", "Nunes", 37)
"""
# Parametro Opcional


"""def imprimir_nome(nome=None, sobrenome=None, idade=None):
    if nome != None:
        print("Nome: ", nome)
        print("Sobrenome: ", sobrenome)
        print("Idade: ", idade)
        print("-------------------------")
    else:
        print("Por favor insira seus dados")
        print("==========================")


imprimir_nome()
"""


# Codigo para Imovel
# Exemplos de numero de argumentos <= numero dos parametros

def imprimir_imovel(nomeImovel, numeroQuartos, vagasGaragem=None):
    print("------------------------")
    print("Titulo: ", nomeImovel)
    print("Quartos: ", numeroQuartos)
    if vagasGaragem != None:
        print("Vagas na garagem: ", vagasGaragem)


imprimir_imovel("Casa 3 Quartos - SP", 3)
imprimir_imovel("Apartamento - MG", 2, 1)
imprimir_imovel("AirBB - BA", 4, 2)

# Exemplos de numero de argumentos > numero dos parametros
#imprimir_imovel("Loja Comercial - ES", 2, 5, "desconto")
