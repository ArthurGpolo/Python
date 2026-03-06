# Ler dois números e exibir o maior 

n1 = int(input("\nForneça o primeiro número: "))
n2 = int(input("Forneça o segundo número: "))

maior = max(n1, n2)
print("O maior número é o:", maior)

# Ler dois números e exibir o maior ou se são iguais

n3 = int(input("\nForneça o primeiro número: "))
n4 = int(input("Forneça o segundo número: "))

maior = max(n3, n4)
if n3 == n4:
    print("Seus números são iguais:", n3, "e", n4)
else:
    print("O maior número é o:", maior)


# Ler três números e exibir o maior 

n5 = int(input("\nForneça o primeiro número: "))
n6 = int(input("Forneça o segundo número: "))
n7 = int(input("Forneça o terceiro número: "))

maior = max(n5, n6, n7)
print("O maior número é o:", maior)