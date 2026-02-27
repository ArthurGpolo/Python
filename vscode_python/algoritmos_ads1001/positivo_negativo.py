# Ler um número e dizer se ele é positivo, negativo ou neutro

#ENTRADA
num = int(input("Forneça um número: "))

#PROCESSAMENTO/SAÍDA
if num > 0: 
    print(num, "é positivo") 
elif num == 0:
    print(num, "é neutro")
else: 
    print(num, "é negativo")