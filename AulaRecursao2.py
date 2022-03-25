# Fatorial sem recursão

def fatorialS(numero):
    fatorial = 1
    if numero == 0:
        return 1
    else:
        for x in range(1, numero + 1):
            fatorial *= x
        return fatorial


print(fatorialS(5))

print("******" * 3)

# Fatorial com recursão


def fatorialR(numero):
    if numero == 0: # Criterio de parada
        return 1
    else:
        # Parametro da chamada recursiva
        return numero * fatorialR(numero - 1)


print(fatorialR(5))
