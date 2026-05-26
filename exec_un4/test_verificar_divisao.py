from verificar_divisao import contar_divisao

def test_contar_divisao():
    try:
        x = int(input("Digite o primeiro número inteiro (x): "))
        y = int(input("Digite o segundo número inteiro (y): "))
        resultado = contar_divisao(x, y)
        if resultado == -1:
            print("Não é possível calcular a divisão por zero.")
        elif resultado == float('inf'):
            print("A divisão é infinita.")
        else:
            print(f"{x} é divisível por {y} um total de {resultado} vezes.")
    except ValueError:
        print("Erro: Entrada inválida. Por favor, digite números inteiros.")

if __name__ == "__main__":
    test_contar_divisao()
