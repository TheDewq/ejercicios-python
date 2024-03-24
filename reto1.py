#reto 1

#calculadora de area y perimetro

import math

def circulo():
    while True:
        r = input("ingresa el radio del circulo: ")
        if r.isnumeric():
            r = int(r)
            break;
        print("el valor ingresado no es un numero")
    return [r**2 * math.pi, 2 * math.pi * r]
def cuadrado():
    while True:
        r = input("ingresa un lado del cuadrado: ")
        if r.isnumeric():
            r = int(r)
            break;
        print("el valor ingresado no es un numero")
    return [r**2, r*4]
    
while True:
    print("cual figura desea usar?")
    print("1] circulo")
    print("2] cuadrado")
    option = input("= ")
    if option.isnumeric():
        option = int(option)
        if option == 1:
            rpt = circulo()
            print("el resultado area es: ")
            print(rpt[0])
            print("el perimetro es: ")
            print(rpt[1])
            break
        if option == 2:
            rpt = cuadrado()
            print("el resultado area es: ")
            print(rpt[0])
            print("el perimetro es: ")
            print(rpt[1])
            break
    print("la opcion ingresada no es valida")


        
    
    
    
