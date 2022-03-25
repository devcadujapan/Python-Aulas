# Deve tomar muito cuidado com os LOOPS INFINITOS

def olamundo():
    print("Ola Mundo")
    olamundo()

#olamundo()

# O Python paralisa a execusao com uma mensagem de erro:
# RecursionError: maximum recursion depth exceeded while calling a Python object

# Loop Infinito eh um ERRO, uma FALHA TECNICA
# Ter muita Atencao com esse tipo de codigo
