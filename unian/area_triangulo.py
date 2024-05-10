import math

def area_triangulo(s1:float, s2:float, s3:float):
    s = sub_perimetro((s1,s2,s3))
    operacion = (s*(s-s1)*(s-s2)*(s-s3))
    return math.sqrt((s*(s-s1)*(s-s2)*(s-s3)))
def sub_perimetro(lados:tuple):
    return ((lados[0]+lados[1]+lados[2])/2)

print("la calculador de triangulos")
rpt = area_triangulo(float(input("ingrese un lado: ")),float(input("ingrese el segundo lado: ")),float(input("ingrese el tercer lado: ")))
print(rpt)