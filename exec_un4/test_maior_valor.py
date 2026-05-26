from maior_valor import maior_valor

def test_maior_valor():
    val1 = float(input("Digite o primeiro valor: "))
    val2 = float(input("Digite o segundo valor: "))
    resultado = maior_valor(val1, val2)
    print(f"O maior valor é: {resultado}")

if __name__ == "__main__":
    test_maior_valor()
