# mult(a, b): multiplicação por somas sucessivas

def entrada(msg):
    e = int(input(msg))
    return e

def mult(a, b):
    cont = 1
    soma = 0
    while cont <= b:
        soma += a
        cont += 1
    return soma

def saida(multiplicacao):
    print(f"Multiplicação = {multiplicacao}")

s1 = entrada("Digite o primeiro valor da soma: ")
s2 = entrada("Digite o segundo valor da soma: ")

multiplicacao = mult(s1, s2)

saida(multiplicacao)