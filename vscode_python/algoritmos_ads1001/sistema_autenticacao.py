user = input("Usuário: ")
if user == "Arthur":
    senha = int(input("Senha: "))
    if senha == 12345:
        print("Acesso permitido")
    else:
        print("Senha incorreta")
else:
    print("Usuário não encontrado")

user_n = input("Digite o novo usuário: ")
match user_n:
    case "Admin":
        senha_n = int(input("Digite a nova senha: "))
        match senha_n:
            case 98765:
                print("Acesso permitido")
            case _:
                print("Senha incorreta")
    case _:
        print("Usuário não encontrado")