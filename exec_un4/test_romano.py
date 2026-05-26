from romano import arabico_para_romano

def test_arabico_para_romano():
    try:
        valor = int(input("Digite um número inteiro de 1 a 50: "))
        print(f"O número {valor} em romano é: ", end="")
        arabico_para_romano(valor)
    except ValueError:
        print("Erro: Entrada inválida. Por favor, digite um número inteiro.")

if __name__ == "__main__":
    test_arabico_para_romano()
