valor_da_compra = float(input("Forneça o valor da compra: "))
peso = float(input("Forneça o peso em kg: "))
tipo_cliente = input("O cliente é premium (s/n): ")

if tipo_cliente not in ["s", "n"] or peso <= 0:
    print("Valor cliente ou peso inválido(s)")
else:
    if tipo_cliente == "s":
        valor_da_compra *= 0.8

    if valor_da_compra > 200:
        frete = 0
    elif peso <= 5:
        frete = 15
    elif peso <= 20:
        frete = 25
    else:
        frete = 50

    total = valor_da_compra + frete

    print(f"Compra: R${valor_da_compra:.2f} | Peso: {peso}kg | Premium: {tipo_cliente}")
    print(f"Frete: R${frete:.2f} | Total: R${total:.2f}")