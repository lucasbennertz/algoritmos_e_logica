def numero_extenso(numero):
    extensos = {
        0: "Zero",
        1: "Um",
        2: "Dois",
        3: "Três",
        4: "Quatro",
        5: "Cinco",
        6: "Seis",
        7: "Sete",
        8: "Oito",
        9: "Nove",
        10: "Dez"
    }
    if numero in extensos:
        print(extensos[numero])
    else:
        print("Erro: Número fora da faixa (0-10)")
