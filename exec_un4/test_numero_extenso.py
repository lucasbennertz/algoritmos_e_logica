from numero_extenso import numero_extenso

def test_numero_extenso():
    try:
        valor = int(input("Digite um número inteiro de 0 a 10: "))
        numero_extenso(valor)
    except ValueError:
        print("Erro: Entrada inválida. Por favor, digite um número inteiro.")

if __name__ == "__main__":
    test_numero_extenso()
