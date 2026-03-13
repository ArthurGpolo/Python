opcao = int(input("Selecione uma das 3 opções\n1 - Somar dois números\n2 - Subtrair dois números\n3 - Multiplicar dois números\n-> "))

match opcao:
    case 1:
        n1 = int(input("Primeiro número: "))
        n2 = int(input("Segundo número: "))
        soma = n1 + n2
        print(f"{soma}")
    case 2:
        n1 = int(input("Primeiro número: "))
        n2 = int(input("Segundo número: "))
        sub = n1 - n2
        print(f"{sub}")
    case 3:
        n1 = int(input("Primeiro número: "))
        n2 = int(input("Segundo número: "))
        mult = n1 * n2
        print(f"{mult}")
    case _:
        print("Opção inválida")