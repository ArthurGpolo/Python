# Recebe uma lista de valores e devolve a média deles 
def calcular_media(valores):
    # Modo 1: iterar sobre os valores da lista
    soma = 0
    for i in valores:
        soma += i
    media1 = soma / len(valores)

    # Modo 2: iterar sobre os índices da lista (corrigido)
    soma = 0 
    for i in range(len(valores)):
        soma += valores[i]
    media2 = soma / len(valores)

    # Modo 3: utilizando funções prontas
    media3 = sum(valores) / len(valores)

    return media1  # pode retornar qualquer uma (todas estão corretas agora)


# Recebe a lista completa de notas e devolve as abaixo da média
def filtro_notas_abaixo_media(valores, nota_minima):
    reprovados = []

    for i in valores:
        if i < nota_minima:
            reprovados.append(i)

    return reprovados


# Classifica uma única nota
def classifica_notas(valor):
    if valor >= 9:
        return 'excelente'
    if valor >= 7:
        return 'bom'
    if valor >= 5:
        return 'regular'
    return 'insuficiente'


# Programa principal
notas = [5, 6, 4, 10]

media = calcular_media(notas)
filtro = filtro_notas_abaixo_media(notas, 6.0)

# Classificar cada nota (corrigido)
classificacoes = [classifica_notas(nota) for nota in notas]

print(f"Média das notas: {media:.2f}")
print(f"Notas abaixo da média: {filtro}")
print(f"Classificação das notas: {classificacoes}")
print(f"Percentual de notas abaixo da mínima: {len(filtro) / len(notas) * 100}%")

# ====================================================================================================================== #

#EXERCÍCIO:

#Suponha que temos agora a lista de nomes que correponde ás notas dadas:
nomes = ["Luís", "José", "Lizandra", "Julia"]

#1. construir uma função que encontra a maior nota
print(f"Maior nota: {max(notas)}")

#2. construir uma função que encontra o nome do aluno que tem a maior nota 
def atribuir_maior_nota_aluno(nomes, notas):
    maior_nota = max(notas)              # encontra a maior nota
    posicao_nota = notas.index(maior_nota)     # encontra a posição dessa nota
    return nomes[posicao_nota]                 # retorna o nome correspondente

aluno = atribuir_maior_nota_aluno(nomes, notas)

print(f"Aluno(a) com a maior nota: {aluno}")

#3. o professor deu um aumento de 20% em cada nota, sem ultrapassar 10
def aumento_20_porcento(nota):
    nova_nota = nota * 1.20
    if nova_nota > 10:
        nova_nota = 10
    return round(nova_nota, 2)

notas_com_aumento = [aumento_20_porcento(nota) for nota in notas]

print(f"Notas com aumento: {notas_com_aumento}")
