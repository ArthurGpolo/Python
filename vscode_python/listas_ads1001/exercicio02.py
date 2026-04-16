# definindo entradas

qtd_notas = int(input("Digite a quantidade de notas: "))

notas = []

# ---------------------------------------------------------------------------------------------------------------------------------- #

# laço while
i = 0
while i < qtd_notas:
    notas.append(float(input(f"Digite a {i + 1}ª nota: ")))
    i = i + 1

print(f"\nSuas notas: {notas}")
print(f"Sua média: {sum(notas) / len(notas)}") # len() == lenght() retornar o número de itens em um objeto
print(f"Sua maior nota: {max(notas)}") # retorna o maior valor entre dois ou mais elementos ou dentro de um iterável
print(f"Sua menor nota: {min(notas)}") # retorna o menor valor entre dois ou mais argumentos, ou o menor elemento de um iterável

