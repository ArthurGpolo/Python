numero = int(input("Digite seus valores, 0 encerra: "))
soma = 0

while numero != 0:
    soma = soma + numero
    print(f"Soma parcial = {soma}")
    numero = int(input("Digite seus valores, 0 encerra: "))
print(f"Soma = {soma}")