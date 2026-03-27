#LER UM NÚMERO INTEIRO, CALCULAR E MOSTRAR O SEU FATORIAL

num = int(input("Digite um número: "))
farorial = 1

for n in range(1 , num + 1, 1):
    farorial = farorial * n  #% pega o resto da divisão
    print(f"Fatorial de {n} é igual a {farorial}\n")

for n in range(4, -3, -1):
    print(f"{n}")
    