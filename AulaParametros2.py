# Argumentos Nomeados

def imprimir_nome(nome, sobrenome, idade):
    print("Nome: ", nome)
    print("Sobrenome: ", sobrenome)
    print("Idade:", idade)


#imprimir_nome("Maria", "Nazare", 25)

#imprimir_nome(sobrenome="Clara", idade=30, nome="Celia")

sobrenome = "Silva"
idade = 43
nome = "Alex"
imprimir_nome(sobrenome=sobrenome, idade=idade, nome=nome)
