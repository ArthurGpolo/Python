# max_min(a,b,c,d)

def entrada(msg):
    e = float(input(msg))
    return e

def maxi(a, b, c, d):
    maximo = max(a, b, c, d)
    return maximo

def mini(a, b, c, d):
    minimo = min(a, b, c, d)
    return minimo

def saidaMaior(maior):
    print(f"Maior = {maior}")

def saidaMenor(menor):
    print(f"Menor = {menor}")

a = entrada("Digite o valor de A: ")
b = entrada("Digite o valor de B: ")
c = entrada("Digite o valor de C: ")
d = entrada("Digite o valor de D: ")

maximo = max(a, b, c, d)
minimo = min(a, b, c, d)

saidaMaior(maximo)
saidaMenor(minimo)