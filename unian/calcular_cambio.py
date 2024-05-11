def calcular_cambio(dinero:int):
    vuelto = ""
    while dinero >= 500:
        vuelto += "A,"
        dinero -= 500
    while dinero >= 200:
        vuelto += "B,"
        dinero -= 200
    while dinero >= 100:
        vuelto += "C,"
        dinero -= 100
    while dinero >= 50:
        vuelto += "D,"
        dinero -= 50
    vuelto = vuelto[:-1]
    return vuelto

