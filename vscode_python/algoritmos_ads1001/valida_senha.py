senha = input("Digite sua senha: ")
contador = 1

while senha != "12345" and contador < 3:
    senha = input(f"Senha inválida digite novamente, você tem {3 -contador} chances: ")
    contador = contador + 1
if senha == "12345":
    print("Acesso permitido")
else:
    print("Contate seu gerente")