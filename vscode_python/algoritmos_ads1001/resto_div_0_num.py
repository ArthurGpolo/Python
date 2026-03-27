num = int(input("Digite um número: "))

for n in range(1 , num + 1, 1):
    if num % n == 0: #% pega o resto da divisão
        print(f"{n}")

    