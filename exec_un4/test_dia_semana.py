from dia_semana import dia_semana

def test_dia_semana():
    try:
        valor = int(input("Digite um número para o dia da semana (1-7): "))
        dia_semana(valor)
    except ValueError:
        print("Erro: Entrada inválida. Por favor, digite um número inteiro.")

if __name__ == "__main__":
    test_dia_semana()
