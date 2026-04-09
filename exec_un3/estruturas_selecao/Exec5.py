valHorasMes = int(input("Digite o número de horas trabalhadas no mês: "))
valNivelProfessor = 0
while valNivelProfessor < 1 or valNivelProfessor > 3:
    valNivelProfessor = int(input("Digite o nível do professor (1 = R$20h/a, 2 = R$25h/a ou 3 = R$30h/a): "))
if valNivelProfessor == 1:
    salario = valHorasMes * 20
elif valNivelProfessor == 2:
    salario = valHorasMes * 25
elif valNivelProfessor == 3:
    salario = valHorasMes * 30
print(f"O salário do professor é: R${salario:.2f}")