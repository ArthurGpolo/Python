# Crie um dicionário chamado funcionario com os seguintes dados:
# nome: "Marina"
# cargo: "Analista de Dados"
# idade: 27
# ativo: True
# Parte 1 – Acesso e Impressão
# Imprima o nome da funcionária.
# Imprima o cargo da funcionária.
# Verifique se a chave "email" está presente no dicionário.
# Use o método get() para acessar a chave "email" com valor padrão "Não informado".

funcionario = {
    "nome": "Maria",
    "cargo": "Analista de Sistemas",
    "idade": 57,
    "ativo": True
}

print("\nParte 1")
print(f"Nome: {funcionario["nome"]}")
print(f"Nome: {funcionario.get("cargo", "Nenhum cargo cadastrado")}")
print(f"Email: {funcionario.get("email", "Nenhum email cadastrado")}")
print("Email:","email\n" in funcionario)

# Parte 2 – Alteração e Inclusão
# Altere o cargo para "Cientista de Dados".
# Adicione um novo campo: "salario" com valor 8500.
# Adicione o campo "email" com o valor "marina@empresa.com".

print("\nParte 2")
funcionario["cargo"] = "Cientista de Dados"

funcionario["salario"] = 8500

funcionario["email"] = "maria@empresa.com"

print(funcionario,"\n")

# Parte 3 – Remoção
# Remova o campo "ativo" usando pop() e mostre o valor removido.

print("Parte 3")
print(f"Valor que saiu: {funcionario.pop("ativo", None)}\n")

# Parte 4 – Iteração
# Percorra o dicionário e imprima todas as chaves.

print("Parte 4")
for chave in funcionario.keys():
    print(chave)
print("")