# caso simples
nome = "Bia"
idade = 18
print(f"{nome} tem {idade} anos.")

a = 3
b = 7
print(f"{a} + {b} = {a + b}")

# acrescentando formatos: {valor: formato}
pi = 3.14159265
print(f"{pi:.3f}") # 3 casas decimais

# número de casas ocupadas
n = 42
m = 136
p = 345667
print(f"m = {m:8}")
print(f"n = {n:8}")
print(f"p = {p:8}")

# alinhamento de texto
texto = "batata"
print(f"| {texto:<12} |") # esquerda
print(f"| {texto:>12} |") # direita
print(f"| {texto:^12} |") # centro

frase = "o rato roeu a roupa do rei de roma"
print(f"| {frase:^12} |") # o limite é ignorado

# preenchimento de caracteres 
n = 3
print(f"n = {n:05}")

# formatação para porcentagem
juros = 0.65789
print(f"taxa = {juros:.3%}")

# separador de milhar
num = 1234567809
print(f"{num:,}")