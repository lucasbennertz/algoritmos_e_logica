from verificar_divisivel import eh_divisivel

def test_eh_divisivel():
    try:
        x = int(input("Digite o primeiro número inteiro (x): "))
        y = int(input("Digite o segundo número inteiro (y): "))
        if eh_divisivel(x, y) == 1:
            print(f"{x} é divisível por {y}.")
        else:
            print(f"{x} não é divisível por {y}.")
    except ValueError:
        print("Erro: Entrada inválida. Por favor, digite números inteiros.")

if __name__ == "__main__":
    test_eh_divisivel()
