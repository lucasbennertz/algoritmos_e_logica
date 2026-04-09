menor = None
maior = None
for i in range(10):
    num = int(input("Digite um número: "))
    if menor is None or num < menor:
        menor = num
    if maior is None or num > maior:
        maior = num
print(f"O menor número é: {menor}")
print(f"O maior número é: {maior}")