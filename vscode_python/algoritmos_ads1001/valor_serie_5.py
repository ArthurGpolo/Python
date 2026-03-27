#LER UM NÚMERO INTEIRO, CALCULAR E MOSTRAR O SEU FATORIAL

num = int(input("Digite um número: "))
soma = 0

for n in range(1, 2 * num, 1):
    if n % 2 == 0:
        print(f"-{n}")
    else:
        print(f"{n}")