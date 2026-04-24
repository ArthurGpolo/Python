# potencia(x, y): potência por multiplicações sucessivas

def entrada(msg):
    e = int(input(msg))
    return e

def pot(base, exp):
    p = 1
    for i in range(exp): # de 0 a exp-1 = exp vezes
        p *= base
    return p

def saida(result):
    print(f"Potênciação = {result}")

base = entrada("Forneça a base: ")
potencia = entrada("Forneça a potência: ")

resultado = pot(base, potencia)

saida(resultado)