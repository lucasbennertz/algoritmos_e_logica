soma = 0
negativos = 0
for i in range(20):
    num = int(input("Digite um número: "))
    soma += num
    if num < 0:
        negativos += 1
print(f"A quantidade de números negativos é: {negativos}")
print(f"A soma dos números é: {soma}")