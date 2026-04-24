# triângulo 
# *
# **
# ***
# n linhas e colunas

def entrada(msg):
    e = int(input(msg))
    return e

def lin_col(l, c):
    n = ""
    for i in range(1, l + 1):
        n += "*" * min(i, c) + "\n"
    return n 

def saida(n):
    print(f"{n}")

linhas = entrada("Forneça a quantidade de linhas: ")
colunas = entrada("Forneça a quantidade de colunas: ")

triangulo = lin_col(linhas, colunas)

saida(triangulo)