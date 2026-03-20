numero = int(input("Digite um valor: "))
soma = 0

while soma < 200:
    soma = soma + numero
    print(f"Soma parcial = {soma}")
    numero = int(input("Digite mais valores: "))
print(f"Soma final = {soma}")