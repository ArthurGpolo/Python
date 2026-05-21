cardapio = {
    "pipoca": 5.00,
    "burguer": 12.00,
    "coca": 7.50
}

carrinho = []

for chave, valor in cardapio.items():
    print(f"{chave}: {valor}")
    quantidade = int(input("Quantos? "))
    if quantidade > 0:
        item = {
            "produto": chave, 
            "valor": valor, 
            "quantidade": quantidade
        }
        carrinho.append(item)
        item = {}

print(f"Carrinho: {carrinho}")

soma = 0

for item in carrinho:
    soma = soma + item["valor"] * item["quantidade"]