nome_produto = input("Informe o nome do produto: ")
peso = float(input("Informe o peso do produto em gramas: "))
preco = float(input("Informe o preço do produto: "))

peso_em_kg = peso * 0.001
preco_por_kg = preco / peso_em_kg 

print(f"\n{nome_produto} | {peso}g | R${preco}")
print(f"{nome_produto} - {peso}g - R${preco} (R${preco_por_kg:.2f}/kg)")