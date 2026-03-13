nota = int(input("Digite sua nota: "))
match nota:
    case 10 | 9:
        print("exelente")
    case 8 | 7:
        print("bom")
    case 6 | 5:
        print("regular")
    case 4 | 3 | 2 | 1 | 0:
        print("insuficiente")
    case _:
        print("Noat inválida")