valA = int(input("Digite o valor de A: "))
valB = int(input("Digite o valor de B: "))
valC = int(input("Digite o valor de C: "))
if valA > valB and valA > valC:
    maior = valA
elif valB > valA and valB > valC:
    maior = valB
elif valC > valA and valC > valB:
    maior = valC
    
if valA < valB and valA < valC:
    menor = valA
elif valB < valA and valB < valC:
    menor = valB
elif valC < valA and valC < valB:
    menor = valC

print(f"A diferença entre o maior valor e o menor valor é: {maior - menor}")