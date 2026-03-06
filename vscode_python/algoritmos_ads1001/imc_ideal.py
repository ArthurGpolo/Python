# Ler o sexo (masculino ou feminino) e a altura de uma pessoa em metros. Calcular o peso ideal :
# masculino: pi = 72.7 x altura - 58
# feminino: p1 = 62.1 x altura - 44.7

#ENTRADAS
sexo = input("Informe seu sexo: ")
altura = float(input("Informe sua altura em metros: "))

#PROCESSAMENTO
if sexo == "masculino":
    imc_ideal = round(altura * 72.7 - 58, 2)
    print("Seu imc ideal é igual a:", imc_ideal)
else:
    imc_ideal = round(altura * 62.1 - 44.7, 2)
    print("Seu imc ideal é igual a:", imc_ideal)
