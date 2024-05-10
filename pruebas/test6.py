num = 0;
while True:
    num = input("ingresa un numero mayor a 0: ")
    if num.isnumeric():
        if int(num) > 0:
            break
    print("el numero ingresado no es valido")
print(num)
num = int(num)
pasos = 0
while num != 1:
    if num % 2 == 0:
        num = num/2
        print(int(num))
        pasos+=1
        continue
    elif num % 2 != 0:
        num = 3 * num + 1
        print(int(num))
        pasos+=1
print("numero de pasos: ",pasos)
        
    
