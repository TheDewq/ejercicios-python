import calculadora_indices as calc

peso = float(input("ingresa tu peso (en Kg): "))
altura = float(input("ingresa tu altura (en Metros): "))
edad = float(input("ingresa tu edad (en años): "))
genero = input("Ingresa tu genero (M - F): ")
if genero == "M":
    genero = 10.8
else:
    genero = 0

print(calc.calcular_porcentaje_grasa(peso, altura, edad, genero))