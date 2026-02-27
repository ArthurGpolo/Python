# Ler: nome do produto, valor unitário e quantidade comprada 
# Calcular o total da compra
# Se a quantidade for maior que 100 definir um desconto de 10%

#ENTRADAS
nome_produto = input("Forneça o nome do produto: ")
valor_unitario = float(input("Forneça o valor unitário do produto: "))
quantidade = int(input("Forneça a quantidade do produto: "))

#PROCESSAMENTO/SAÍDA
total_da_compra = quantidade * valor_unitario
total_da_compra_arredondado = round(total_da_compra, 2)

desconto = 0.1 * total_da_compra 
desconto_arredondado = round(desconto, 2)

total_da_compra_com_desconto = total_da_compra_arredondado - desconto_arredondado

if quantidade > 100:
    print("\nA compra de", nome_produto, "com desconto é igual a R$",total_da_compra_com_desconto)
else: 
    print("\nA compra de", nome_produto, "é igual a R$",total_da_compra_arredondado)