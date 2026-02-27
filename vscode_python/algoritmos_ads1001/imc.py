#Cálculo do IMC:

#ENTRADAS
altura = float(input('Forneça sua altura em metros: '))
peso = float(input('Forneça seu peso em kilogramas: '))

#PROCESSAMENTO
imc = peso / (altura * altura)
imc_arredondado = round(imc, 2)

#PROCESSAMENTO/SAÍDA
if imc_arredondado < 18.5:
    print("\nVocê está abaixo do peso")
elif 18.5 <= imc_arredondado < 25:
    print("\nVocê está no peso normal")
else:
    print("\nVocê está acima do peso")