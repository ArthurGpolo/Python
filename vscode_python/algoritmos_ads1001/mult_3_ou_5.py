soma = 0 

for n in range(0, 1000, 1):
    if n % 3 == 0 or n % 5 == 0: #% pega o resto da divisão
        soma = soma + n
        print(f"{soma}")

    