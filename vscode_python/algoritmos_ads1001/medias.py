# Uma professora precisa de um programa que ajuda a calcular a médial final dos alunos e informe se foram aprovados, ficaram de recuperação ou reprovados. As regras são:
# Média >= 7: Aprovado 
# 5 <= Média <7: Recuperação
# Média < 5 Reprovado
# Escreva um programa que recebe três notas como entrada e calcula a média final.
# Com base na média, exiba a situação do aluno.

#ENTRADAS
nota1 = float(input("Forneça a primeira nota: "))
nota2 = float(input("Forneça a segunda nota: "))
nota3 = float(input("Forneça a terceira nota: "))

#PROCESSAMENTO
media = (nota1 + nota2 + nota3) / 3
media_arredondada = round(media, 2)

#PROCESSAMENTO/SAÍDA
print("\nSua média é", media_arredondada)
if media_arredondada >= 7:
    print("Você está Aprovado")
elif 5 <= media_arredondada < 7:
    print("Você está de Recuperação")
else:
    print("Você está Reprovado")