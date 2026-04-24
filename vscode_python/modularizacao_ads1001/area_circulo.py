import math

def entrada(msg):
    raio = float(input(msg))
    return raio

def area(raio):
    a = math.pi * (raio**2)
    return a

def saida(n, area):
    print(f"Área {n} = {area:.2f}")

r1 = entrada("Digite o valor do raio 1: ")
area1 = area(r1)
saida(1, area1)

r2 = entrada("Digite o valor do raio 2: ")
area2 = area(r2)
saida(2, area2)