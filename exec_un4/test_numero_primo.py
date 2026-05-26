from numero_primo import eh_primo

def test_eh_primo():
    try:
        num = int(input("Digite um número inteiro para verificar se é primo: "))
        if eh_primo(num) == 1:
            print(f"O número {num} é primo.")
        else:
            print(f"O número {num} não é primo.")
    except ValueError:
        print("Erro: Entrada inválida. Por favor, digite um número inteiro.")

if __name__ == "__main__":
    test_eh_primo()
