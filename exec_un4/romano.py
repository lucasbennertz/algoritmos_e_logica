def arabico_para_romano(numero):
    if not (1 <= numero <= 50):
        print("Erro: Número fora da faixa (1-50)")
        return

    val = [
        40, 10, 9, 5, 4, 1
    ]
    syb = [
        "XL", "X", "IX", "V", "IV", "I"
    ]
    
    # Adicionando os valores e símbolos para 50
    if numero == 50:
        print("L")
        return
        
    romano_num = ""
    i = 0
    while numero > 0:
        for _ in range(numero // val[i]):
            romano_num += syb[i]
            numero -= val[i]
        i += 1
    print(romano_num)
