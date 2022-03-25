"""
numeroInt = 5
while numeroInt > 0:
    print(numeroInt)
    numeroInt -= 1
print("-----" * 5)


def reduzirNumero(numeroInt):
    while numeroInt > 0:
        print(numeroInt)
        numeroInt -= 1


reduzirNumero(5)
"""
"""
Algoritmo
1 - Checar se o nosso numero não é igual a 0
2 - Se ele não for igual a 0 - reduzir 1 unidade

5 (N - 1)
 4 (5 - 1)
  3 (4 - 1)
   2 (3 - 1)
    1 (2 - 1)
     0 (1 - 1)
"""


def reduzirNumero(numeroInt):
    print(numeroInt)
    if numeroInt > 0:
        # N - 1
        reduzirNumero(numeroInt - 1)


reduzirNumero(5)
