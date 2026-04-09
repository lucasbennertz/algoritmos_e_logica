valLadoA = int(input("Digite o valor do lado A: "))
valLadoB = int(input("Digite o valor do lado B: "))
valLadoC = int(input("Digite o valor do lado C: "))

if valLadoA > valLadoB + valLadoC or valLadoB > valLadoA + valLadoC or valLadoC > valLadoA + valLadoB:
    print("Os valores não formam um triângulo.")
elif valLadoA == valLadoB and valLadoA == valLadoC:
    print("O triângulo é equilátero.")
elif valLadoA == valLadoB or valLadoA == valLadoC or valLadoB == valLadoC:
    print("O triângulo é isósceles.")
else:
    print("O triângulo é escaleno.")
