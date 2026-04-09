moradores = int(input("Digite o número de moradores: "))
custoKwh = float(input("Digite o custo por kWh: "))
valores = []
total = 0
for i in range(moradores):
    consumo = float(input(f"Digite o consumo de kWh do morador {i + 1}: "))
    custo = consumo * custoKwh
    valores.append(custo)
    total += custo
for i in range(moradores):
    print(f"O custo do morador {i + 1} é: R${valores[i]:.2f}")
print(f"O custo total é: R${total:.2f}")
