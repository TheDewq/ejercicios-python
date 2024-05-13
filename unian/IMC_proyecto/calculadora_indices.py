
def calcular_IMC(peso:float, altura:float): #:float
    return peso/(altura**2)

def calcular_porcentaje_grasa(peso:float, altura:float, edad:int, valor_genero:float): #:float
    return 1.2*calcular_IMC(peso, altura)+0.23*edad-5.4-valor_genero

def calcular_calorias_en_reposo(peso:float, altura:float, edad:int, valor_genero:int): #:float
    return (10*peso) + (6.25*altura*100) - (5*edad) + valor_genero

def calcular_calorias_en_actividad(peso:float, altura:float, edad:int, valor_genero:int, valor_actividad:float): #:float
    return calcular_calorias_en_reposo(peso, altura, edad, valor_genero) * valor_actividad

def consumo_de_calorias_recomendado(peso:float, altura:float, edad:int, valor_genero:int): #:str
    #falta
    return None