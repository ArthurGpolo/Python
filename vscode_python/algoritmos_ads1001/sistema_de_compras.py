print("Sistema de compras ByMauá!")

#ENTRADA
valor_compra = float(input("Informe o valor da compra: "))
opcao_de_pagamento = int(input("Digite \n1 para pagamento a vista \nou \n2 para pagamento a prazo \n-> "))

#PROCESSAMENTO/SAÍDA
if opcao_de_pagamento == 1:
    forma_pagamento = int(input("\nSelecione a forma de pagamento:\nDigite 1 para PIX \nou \nDigite 2 para Boleto\n ->"))
    if forma_pagamento == 1:
        desconto = 0.1 * valor_compra 
        valor_final = valor_compra - desconto
        print("Parabéns, para pagamento a vista no PIX, você tem")
        print("Desconto =", round(desconto, 2), "e o valor a pagar =", round(valor_final, 2))
    elif forma_pagamento == 2:
        desconto = 0.05 * valor_compra 
        valor_final = valor_compra - desconto
        print("Parabéns, para pagamento a vista no Boleto, você tem")
        print("Desconto =", round(desconto, 2), "e o valor a pagar =", round(valor_final, 2))
    else:
        print("Forma de pagamento inválida")
elif opcao_de_pagamento == 2:
    parcelas = int(input("Digite o número de parcelas (2/3): "))
    if parcelas == 2:
        valor_parcela = valor_compra / 2
        print("Valor parcela =", round(valor_parcela, 2), "valor final =", round(valor_compra, 2))
    elif parcelas == 3:
        acrescimo = valor_compra * 0.05
        valor_parcela = valor_compra / 3 
        parcela_acrescimo = valor_parcela * 0.05
        parcela_final = valor_parcela + parcela_acrescimo
        valor_final = valor_compra + acrescimo
        print("Valor parcela =", round(parcela_final, 2), "valor final com acrescimo de 5% =", round(valor_final, 2))
    else:
        print("Número de parcelas inválido")
else:
    print("Opção de pagamento inválida")