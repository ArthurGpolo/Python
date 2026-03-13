peso_pacote = float(input("Digite o peso do pacote em kg: "))
if  0 < peso_pacote <= 1:
    frete = "Tipo de frete = leve"
elif 1 < peso_pacote <= 5:
    frete = "Tipo de frete = normal"
elif 5 < peso_pacote <= 10:
    frete = "Tipo de frete = pesado"
elif peso_pacote > 10:
    frete = "Tipo de frete = especial"
else:
    frete ="Peso inválido"

print(f"{frete}")