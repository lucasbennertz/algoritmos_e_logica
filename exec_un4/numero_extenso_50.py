def extenso_50(numero):
    if not (0 <= numero <= 50):
        return "Erro: Número fora da faixa (0-50)"

    unidades = ["zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"]
    especiais = {10: "dez", 11: "onze", 12: "doze", 13: "treze", 14: "catorze", 15: "quinze", 16: "dezesseis", 17: "dezessete", 18: "dezoito", 19: "dezenove"}
    dezenas = ["", "", "vinte", "trinta", "quarenta", "cinquenta"]

    if 0 <= numero <= 9:
        return unidades[numero]
    elif 10 <= numero <= 19:
        return especiais[numero]
    elif 20 <= numero <= 50:
        dezena, unidade = divmod(numero, 10)
        if unidade == 0:
            return dezenas[dezena]
        else:
            return f"{dezenas[dezena]} e {unidades[unidade]}"
