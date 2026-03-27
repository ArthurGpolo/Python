#ENTRADA DE DADOS
inicio = int(input("Digite o valor inicial do intervalo: "))
fim = int(input("Digite o valor final do intervalo: "))

#VALIDAR A ENTRADA
if inicio > fim:
    auxiliar = inicio
    inicio = fim 
    fim = auxiliar
    
#AJUSTAS O FIM
fim = fim + 1

#INICIALIZANDO OS ACUMULADORES
soma = 0
multiplicacao = 1

#LAÇO
for n in range(inicio, fim, 1):
    if n % 2 == 0: #% pega o resto da divisão
        soma = soma + n
    else:
        multiplicacao = multiplicacao * n

#SAÍDA
print(f"Soma = {soma}\nMultiplicação = {multiplicacao}")
    