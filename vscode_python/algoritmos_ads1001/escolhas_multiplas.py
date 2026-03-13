# ler um número de 1 a 5 e exibilo por extenço
num = int(input("Digite um valor de 1 a 5: "))
if num == 1:
    print("um")
elif num == 2:
    print("dois")
elif num == 3:
    print("tres")
elif num == 4:
    print("quatro")
elif num == 5:
    print("cinco")
else:
    print("Valor inválido")

# utilizando match-case
match num:
    case 1:
        print("um")
    case 2:
        print("dois")
    case 3:
        print("tres")
    case 4:
        print("quatro")
    case 5:
        print("cinco")
    case _:
        print("Valor inválido")

nome = "Gil"
match nome:
    case "Ana":
        print("Banana")
    case "João":
        print("Balão")
    case "Gil":
        print("match")
    