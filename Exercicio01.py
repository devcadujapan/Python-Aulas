def o_maior(x, y):
    print("X = ", x)
    print("Y = ", y)
    if x > y:
        return x
    elif y > x:
        return y


print("O Maior é: ", (o_maior(10, -10)))
