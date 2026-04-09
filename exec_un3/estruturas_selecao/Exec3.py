valA = int(input("Digite o valor de A: "))
valB = int(input("Digite o valor de B: "))
valC = int(input("Digite o valor de C: "))
if valA > valB and valA > valC:
    print("O valor de A é o maior entre os três valores.")
elif valB > valA and valB > valC:
    print("O valor de B é o maior entre os três valores.")
elif valC > valA and valC > valB:
    print("O valor de C é o maior entre os três valores.")
    
if valA < valB and valA < valC:
    print("O valor de A é o menor entre os três valores.")
elif valB < valA and valB < valC:
    print("O valor de B é o menor entre os três valores.")
elif valC < valA and valC < valB:
    print("O valor de C é o menor entre os três valores.")