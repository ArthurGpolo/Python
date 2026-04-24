# Triângulo(n)
# *
# * *
# * * *
# n linhas e colunas
n = int(input("Quantas linhas você quer?\n--> "))
for linha in range(1, n + 1):
    for coluna in range(1, linha + 1):
        print(coluna, end = "")
    print("")