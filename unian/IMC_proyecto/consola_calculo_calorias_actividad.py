import calculadora_indices as calc

peso = float(input("ingresa tu peso (en Kg): "))
altura = float(input("ingresa tu altura (en Metros): "))
edad = float(input("ingresa tu edad (en años): "))
genero = input("Ingresa tu genero (M - F): ")
valor_actividad = float(input("ingresa el valor de actividad: "))
if genero == "M":
    genero = 5
else:
    genero = -161

print(calc.calcular_calorias_en_actividad(peso, altura, edad, genero,valor_actividad))