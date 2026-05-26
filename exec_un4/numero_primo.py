def eh_primo(numero):
    if numero <= 1:
        return 0
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return 0
    return 1
