def classifica_senha(tamanho):
    if tamanho < 6:
        categoria = "Fraca"
    elif tamanho < 10:
        categoria = "Média"
    else:
        categoria = "Forte"

    return categoria

tamanho = int(input("Quantos caracteres tem sua senha: "))

resultado = classifica_senha(tamanho)

print(f"Sua senha é: {resultado}")