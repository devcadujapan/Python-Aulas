# Paradima Imperativo
# Imperare >> Comandar
# variáveis, atribuições e sequências
# C, Fortran, Cobol, Basic, Pascal, Ada, Modula-2
# Scopo -- codigos limitados num arquivo

#bloco externo
nome = "Gabriel" #variavel global

#quebrar 2 linhas para uma funcao
def minha_funcao():
    #bloco interno >bloco interno de uma funcao é conhecido como corpo da função
    nome = "Ana" #variavel local
    tupla = 2, 5, 6, 8, 1
    print(tupla)
    print(nome)
    if nome == "Ana":
        print("Impressao do bloco interno da condicao if")
    for x in tupla:
        print(x)

#quebrar 2 linhas no fim do bloco
print(nome)
minha_funcao()
