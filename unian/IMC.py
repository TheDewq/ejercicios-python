def calcular_BMI(peso_lb:float, altura_inch:float):
    return peso_lb/(altura_inch)

print("calculadora de IMC")
print(calcular_BMI(float(input("ingrese su peso en libras: ")),float(input("ingrese su altura en pulgadas: "))))