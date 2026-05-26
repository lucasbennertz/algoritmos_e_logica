from numero_extenso_50 import extenso_50

def test_extenso_50():
    try:
        valor = int(input("Digite um número inteiro de 0 a 50: "))
        resultado = extenso_50(valor)
        print(f"O extenso de {valor} é: {resultado}")
    except ValueError:
        print("Erro: Entrada inválida. Por favor, digite um número inteiro.")

if __name__ == "__main__":
    test_extenso_50()
