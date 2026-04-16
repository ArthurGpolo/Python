# definindo entradas

n = int(input("Digite quantos pares você quer: "))

# ------------------------------------------------------------------------------------------------------------ #

# laço while
pares = [] # inicializa uma lista vazia chamada "pares"

cont = 0
while cont < n:
    pares.append(2 * cont) # adiciona um único elemento ao final de uma lista
    cont = cont + 1

print(f"\nPares: {pares}")
print(f"Soma: {sum(pares)}") # soma os elementos de um iterável (como listas, tuplas ou conjuntos).

# ------------------------------------------------------------------------------------------------------------ #

# laço for
pares = [] # reinicializa a lista "pares" para tornala vazia denovo

for i in range(2 * n): # usado para gerar uma sequência de números, sendo amplamente utilizada em loops.
    if i % 2 == 0:
        pares.append(i)

print(f"\nPares: {pares}")
print(f"Soma: {sum(pares)}")

# ------------------------------------------------------------------------------------------------------------ #

# laço for otimizado
pares = [] # reinicializa a lista "pares" para tornala vazia denovo

for i in range(0, 2 * n, 2):
    pares.append(i)

print(f"\nPares: {pares}")
print(f"Soma: {sum(pares)}")

# ------------------------------------------------------------------------------------------------------------ #

# método de uma linha só com pior desempenho
pares = [i for i in range(2 * n) if i % 2 == 0] # reinicializa a lista "pares" e defini seus valores

print(f"\nPares: {pares}")
print(f"Soma: {sum(pares)}")