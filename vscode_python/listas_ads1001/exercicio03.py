# definindo entradas

agenda = []

# ---------------------------------------------------------------------------------------------------------------------------------- #

while True: # laço infinito no python
    print("\n------ Agenda ------")
    print("1 - Cadastrar nome")
    print("2 - Remover nome")
    print("3 - Alterar nome")
    print("4 - Buscar nome")
    print("5 - Mostrar agenda")
    print("6 - Ordenar agenda (A-Z)")
    print("7 - Ordenar agenda (Z-A)")
    print("0 - Sair")
    print("--------------------")
    opcao = int(input("Digite sua opção: "))
    match opcao:
        case 1:
            nome = input("Forneça um nome: ")
            agenda.append(nome) # adiciona um nome na agenda
            print(f"{nome} cadastrado com sucesso!")
        case 2:
            nome = input("Forneça um nome: ")
            if nome in agenda: # in == se estiver na agenda
                agenda.remove(nome) # remove um nome na agenda
                print(f"{nome} removido com sucesso!")
            else:    
                print(f"{nome} não consta na agenda")
        case 3:
            nome_antigo = input("Digite o nome a ser alterado: ")
            if nome_antigo in agenda:
                posicao = agenda.index(nome_antigo) # descobre em qual posição o item está na agenda
                nome_novo = input("Qual o novo nome: ")
                agenda[posicao] = nome_novo
                print(f"{nome_antigo} alterado para {nome_novo} com sucesso!")
            else:
                print(f"{nome_antigo} não consta na agenda")
        case 4:
            nome = input("Forneça um nome a ser encontrado: ")
            if nome in agenda:
                posicao = agenda.index(nome)
                print(f"{nome} se encontra na {posicao + 1}ª posição da agenda de contatos") 
            else:
                print(f"{nome} não consta na agenda de contatos")
        case 5:
            if len(agenda) == 0:
                print("Agenda vazia")
            else:
                print(f"Agenda: {agenda}")
        case 6:
            if len(agenda) == 0:
                print("Agenda vazia")
            else:
                print(f"Agenda (A-Z): {sorted(agenda)}")
        case 7:
            if len(agenda) == 0:
                print("Agenda vazia")
            else:
                print(f"Agenda (Z-A): {list(reversed(sorted(agenda)))}")
        case 0:
            print("Obrigado, volte sempre")
            break # quebra o laço infinito
        case _: # caso o usuário digitar alguma coisa que não está nas opções
            print("Opção inválida")