# Recebe uma lista de valores e devolve a média deles
def calcular_media (valores):
    
    #  Método 1: Iterar sobre os valores da lista
    soma = 0
    for v in valores:
        soma = soma + v
    media1 = soma / len(valores)
    
    # Método 2: Iterar sobre os índices da lista
    soma = 0
    for i in range(len(valores)):
        soma = soma + valores[i]
    meida2 = soma / len(valores)
    
    #  Método 3: Utilizando as funções de lista
    media3 = sum(valores) / len(valores)
    
    return media3

# Receber a lista completa de notas e devolver a lista de notas abaixo da nota mínima
def filtro_notas_abaixo_media (valores, nota_minima):
    
    reprovados = []
    for v in valores:
        if v < nota_minima:
            reprovados.append(v)
    return reprovados

# Recebe uma nota e classifica em "Bom, Regular , Excelente e Insuficiente"
def classifica_nota (valor):
    
    if valor >= 9: return "Excelente"
    if valor >= 7: return "Bom"
    if valor >= 5: return "Regular"
    return "Insuficiente"

# Define a maior nota (max) da uma lista selecionada
def maior_nota (notas):
    maior_nota = max(notas)
    return maior_nota

# Verifica todos valores das listas valores e nomes e entrega apenas o nome do melhor aluno 
def melhor_aluno (valores, nomes):
    maior_nota = valores[0]
    melhor_aluno = nomes[0]
    for i in range(1, len(valores)):
        if valores[i] > maior_nota:
            maior_nota = valores[i]
            melhor_aluno = nomes[i]
    return melhor_aluno


# Programa principal
notas = [5, 6, 4, 10]
media = calcular_media(notas)

# Mesma coisa de maneiras diferentes
print(f"Média dos alunos: {media:.2f}")
print(f"Média dos alunos: {calcular_media(notas):.2f}")

print(f"A média da turma foi: {classifica_nota(media)}")

abaixo_minimo = filtro_notas_abaixo_media(notas, 6.0)
print(f"Notas abaixo do mínimo: {filtro_notas_abaixo_media(notas, 6.0)}")
print(f"Tivemos {len(abaixo_minimo)} notas abaixo da nota mínima")

print(f"Percentual de notas abaixo da mínima: {len(abaixo_minimo) / len(notas) * 100}%")

# Suponha que temos agora a lista de nomes que correpsondem às notas dadas:
nomes = ["Luis", "João", "Lizandra", "Julia"]

# 1 - Contruir uma função que encontra a maior nota
print(f"A maior nota foi: {maior_nota(notas)}")

# 2 - Construir uma função que encontra o nome do aluno que tem a maior nota
print(f"O melhor aluno é: {melhor_aluno(notas, nomes)}")

# 3 - O professor ficou muito bonzinho e fez um acréscimo de 20% em cada nota, sem ultrapassar 10
# Criar uma função que recebe a lista de notas e a altera acrescentando os 20%, sem ultrapassar 10
# print(f"As notas após o acrescimo serão: {acrescimo_nota(notas)}")