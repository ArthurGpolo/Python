valor_total_conta = float(input("Forneça o valor total da conta: "))
percentual_gorjeta = float(input("Forneça o percentual da gorjeta: "))
num_pessoas = int(input("Forneça o número de pessoas: "))

valor_gorjeta = (percentual_gorjeta / 100) * valor_total_conta
compra_com_gorjeta = valor_gorjeta + valor_total_conta
qtd_cada_pessoa_paga = compra_com_gorjeta / num_pessoas

print(f"Conta: R${valor_total_conta} | Gorjeta: {percentual_gorjeta:.0f}% | Pessoas: {num_pessoas}")
print(f"Gorjeta: R${valor_gorjeta:.2f} | Total: R${compra_com_gorjeta} | Por pessoa: R${qtd_cada_pessoa_paga:.2f}")