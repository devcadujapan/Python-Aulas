"""lista = [1, 2, 3, 4, 5]
print(lista)

retorno = lista.pop()
var1 = print("Ola Mundo")
print(lista)
print("Retorno da funcao pop: ", retorno)
print("Retorno da funcao print: ", var1)"""

"""
def ola_mundo():
    return "Ola Mundo"


print(ola_mundo())
"""

# Para nao dar erro no codigo sem terminar uma definicao

"""def par_impar():
    pass"""


# Definindo se o numero é Par ou Ímpar

def par_impar():
    numero = 23
    if (numero % 2) == 0:
        return "Numero par"
    return "Numero ímpar"


print(par_impar())
