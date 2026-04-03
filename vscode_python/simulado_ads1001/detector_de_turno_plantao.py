hora = int(input("Informe uma hora de 0 a 23: "))

if hora > 23 or hora < 0:
    print("Valor inválido")
elif hora >= 6 and hora < 14:
    print(f"{hora} -> Turno da manhã")
elif hora >= 14 and hora < 23:
    print(f"{hora} -> Turno da tarde")
else:
    print(f"{hora} -> Turno da noite")