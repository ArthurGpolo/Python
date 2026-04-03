contador = 0
soma = 0

x = int(input("Forneça o IAQ (-1 para encerrar): "))

if x != -1:
    minimo = x
    maximo = x
    leituras = contador

    while x != -1:
        soma = soma + x
        contador = contador + 1

        if x < minimo:
            minimo = x
        if x > maximo:
            maximo = x

        x = int(input("Forneça o IAQ (-1 para encerrar): "))

    media = soma / contador

    print(f"Leituras: {contador} | Média: {media:.2f} | Mín: {minimo} | Máx: {maximo}")
else:
    print("Nenhuma leitura foi fornecida.")