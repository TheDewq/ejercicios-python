import calculadora_indices as calc

peso = float(input("ingresa tu peso (en Kg): "))
altura = float(input("ingresa tu altura (en Metros): "))
edad = float(input("ingresa tu edad (en años): "))
genero = input("Ingresa tu genero (M - F): ")
if genero == "M":
    genero = 5
else:
    genero = -161

print(calc.calcular_calo81rias_en_reposo(peso, altura, edad, genero))