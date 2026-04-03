char = input("Forneça um caractere: ")
largura = int(input("Forneça a largura: "))
altura = int(input("Forneça a altura: "))

char_largura = char * largura

char_meio = char + " " * (largura - 2) + char

print(f"Char: {char} | Largura: {largura} | Altura: {altura}")

print(char_largura)
for i in range(altura - 2):
    print(char_meio)
print(char_largura)