def numeros(num1, num2):
    num1 = float
    num2 = float
    sinal = str
    if sinal == "+":
        (num1 + num2)
    elif sinal == "-":
        (num1 - num2)
    elif sinal == "*":
        (num1 * num2)
    elif sinal == "/":
        (num1 / num2)
    elif sinal == "**":
        (num1 ** num2)
    return numeros(sinal)


numeros()
