def dia_semana(numero):
    dias = {
        1: "DOM",
        2: "SEG",
        3: "TER",
        4: "QUA",
        5: "QUI",
        6: "SEX",
        7: "SAB"
    }
    if numero in dias:
        print(dias[numero])
    else:
        print("Erro: Número não corresponde a um dia da semana (1-7)")
