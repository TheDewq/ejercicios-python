#programa tiktaktoe

import sys
import random

global p #puestos de la tabla (se uso p por practicidad)
global poc
p = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
poc = [0,1,2] #posiciones del arreglo puestos
def print_line():
    print("+-------+-------+-------+")
def print_space():
    print("|       |       |       |")
def print_tabla():
    for i in range(len(p)):
        print_line()
        print_space()
        print("|   "+str(p[i][0])+"   |   "+str(p[i][1])+"   |   "+str(p[i][2])+"   |")
        print_space()
    print_line()
    
def endp(x): #X>com;O>usr
    if x == "X":
        print("perdiste")
        sys.exit()
    else:
        print("ganaste")
        sys.exit()
def determinar_ganador():
    for i in range(3):
        if p[0][i] == p[1][i] and p[1][i] == p[2][i]: #verificar lineas verticales
            endp(p[0][i])
    for i in range(len(p[0])):
        if p[i][0] == p[i][1] and p[i][1] == p[i][2]: # verificar horizantales
            endp(p[i][0])
    if p[0][0] == p[1][1] and p[1][1] == p[2][2]:#verficar linea desde 0,0 hasta 2,2
        endp(p[0][0])
    if p[0][2] == p[1][1] and p [1][1] == p[2][0]:# verificar linea desde 0,2 hasta 2,0
        endp(p[0][2])
def jugada_com():
    while True:
        x = random.choice(poc)
        y = random.choice(poc)
        print(p[x][y])
        if p[x][y] != "X":
            p[x][y] = "X"
            break
            

def jugada_usr():
    print("tu turno")
    x = int(input("Ingrese un numero del 1-9"))
    for i in range(len(p)):
        for y in range(len(p)):
            if p[i][y] != "O" and p[i][y] == x:
                p[i][y] = "O"

print("Bienvenido al tic-tac-toe (triki por si eres de chibchombia)")

while True:
    print_tabla()
    jugada_com()
    print_tabla()
    jugada_usr()
    determinar_ganador()
    3