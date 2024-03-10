import random

list = [1,2,3,4,5,6,7,8,9]
secret_number = random.choice(list)
x= -1
while secret_number != x:
    print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
    x = int(input("ingresa un numero para salir del bucle: "))
print("¡Bien hecho, mugr! Eres libre ahora.")
    
