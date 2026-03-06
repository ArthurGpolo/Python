#ENTRADA
tipo_ingresso = int(input("Escolha o tipo do ingresso:\n Digite 1 para pista\n Digite 2 para arquibancada\n -> "))

#PROCESSAMENTO/SAÍDA
if tipo_ingresso == 1:
    qtd_ingresso = int(input("\nInforme a quantidade de ingressos: "))
    ingresso_pista = input("Escolha a classe do ingresso da pista:\n Diigite P para premium\n Digite C para comum\n -> ")
    if ingresso_pista == "P":
        valor_pago = qtd_ingresso * 500
        print("O valor a ser pago é de:", valor_pago)
    elif ingresso_pista == "C":
        valor_pago = qtd_ingresso * 200
        print("O valor a ser pago é de:", valor_pago)
    else:
        print("Classe do ingresso inválida")
elif tipo_ingresso == 2:
    qtd_ingresso = int(input("\nInforme a quantidade de ingressos: "))
    ingresso_arquibancada = input("Escolha a classe do ingresso da arquibancada:\n Diigite S para superior\n Digite I para inferior\n -> ")
    if ingresso_arquibancada == "S":
        valor_pago = qtd_ingresso * 350
        print("O valor a ser pago é de:", valor_pago)
    elif ingresso_arquibancada == "I":
        valor_pago = qtd_ingresso * 400
        print("O valor a ser pago é de:", valor_pago)
    else:
        print("Classe do ingresso inválida")
else:
    print("Tipo de ingresso inválido")