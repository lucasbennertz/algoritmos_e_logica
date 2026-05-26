from mes_correspondente import mes_correspondente

def test_mes_correspondente():
    try:
        valor = int(input("Digite um número inteiro para o mês: "))
        mes_correspondente(valor)
    except ValueError:
        print("Erro: Entrada inválida. Por favor, digite um número inteiro.")

if __name__ == "__main__":
    test_mes_correspondente()
