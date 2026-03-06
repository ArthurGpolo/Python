import math

# ENTRADA
a = float(input("Forneça o valor de a: "))
b = float(input("Forneça o valor de b: "))
c = float(input("Forneça o valor de c: "))

# PROCESSAMENTO/SAÍDA
delta = (b ** 2) - 4 * a * c

if a == 0:
    print("não é equação do segundo grau")
elif delta < 0:
    print("x não tem raiz real")
elif delta == 0:
    x = -b / (2 * a)
    print("x possui uma raiz real:")
    print("x =", x)
else:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print("x possui duas raízes reais:")
    print("x1 =", x1)
    print("x2 =", x2)