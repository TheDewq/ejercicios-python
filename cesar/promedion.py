


def new_number_confirmation():
    temp = input("desea ingresar un nuevo numero? [Y] = Si [N] = No -> ")
    if temp == "Y" or temp == "y":
        return False
    elif temp == "N" or temp == "n":
        return True
    else:
        print("respuesta no valida")
        return new_number_confirmation()

def input_new_number():
    print("ingresa un numero")
    temp = input("= ")
    if temp.isnumeric():
        return int(temp)
    else:
        print("el valor ingresado no es valido")
        return input_new_number()
    
def calcular_promedio(list:tuple):
    suma = 0
    for a in list:
        suma = suma + a
    return suma/len(list)


###############     bloque principal    ###############
valores = []
print("Calculadora de promedios")
while True:
    valores.append(input_new_number())
    if new_number_confirmation():
        break
print("el promedio de los valores ingresado es: "+str(calcular_promedio(valores)))

