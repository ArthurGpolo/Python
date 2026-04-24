def divisao(dividendo, divisor):
    quociente = dividendo // divisor
    resto = dividendo % divisor
    return quociente, resto

a = int(input("Dividendo: "))
b = int(input("Divisor: "))

q, r = divisao(a, b)

print(f"Quociente = {q}\nResto = {r}")