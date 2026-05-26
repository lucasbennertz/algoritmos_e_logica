def contar_divisao(x, y):
    if y == 0:
        return -1
    if y == 1 and x != 0:
        return float('inf')
    if x == 0:
        return float('inf')
    if y == x:
        return 1
    
    contador = 0
    while x > 0 and x % y == 0:
        x //= y
        contador += 1
    
    return contador
