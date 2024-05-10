nBloques = int(input("ingrese el numero de bloques"))
pisos = 0;
i = 1;
while True:
    if i <= nBloques:
        pisos= pisos + 1
        nBloques = nBloques - i
        i = i + 1
    else:
        break
print("el numero de pisos es ",pisos)
    
