#reto 2
#el tipico programa de inventarios

inventario = [["celular",1000000, 3]];

def mostrar_inventario():
    print ("# - nombre - precio - catidad")
    for i in range(len(inventario)):
        print(i+1,inventario[i][0],inventario[i][1],inventario[i][2],sep=" - ")
    
def agregar():
    producto = [];
    producto.append(input("Ingrese el nombre del producto: "))
    while True:
        temp = input("Ingrese el precio del producto: ")
        if temp.isnumeric():
            if int(temp) > 0:
                producto.append(int(temp))
                break
        print("no se ingreso un numero valido")
    while True:
        temp = input("Ingrese la cantidad del producto: ")
        if temp.isnumeric():
            if int(temp) > 0:
                producto.append(int(temp))
                break
        print("no se ingreso un numero valido")
    inventario.append(producto)
    print("el prodcuto fue agregado exitosamente")
    
def actualizar():
    print("Cual producto desea actualizar?")
    mostrar_inventario();
    while True:
        temp = input("= ")
        if temp.isnumeric():
            if int(temp) > 0:
                temp -= 1
                break
        print("no se ingreso un numero valido")
    print("nuevo nombre (si no desea modificarlo presione enter")
    x = input("= ")
    if x != "":
        inventario[temp][0] = x
    print("nuevo cantidad (si no desea modificarlo presione enter")
    x = input("= ")
    if x != "":
        inventario[temp][0] = x
    
#def valor_total():





print("bienvenido al sistema gestor de invetarios!")
print("que accion desear realizar?")
while True:
    print("1] Agregar producto")
    print("2] Actualizar un producto")
    print("3] Generar valor total de todos los productos")
    print("4] Mostrar todo el inventario")
    option = input("= ")
    if option.isnumeric():
        option = int(option)
        if option == 1:
            agregar()
        #if option == 2:

        #if option == 3:

        if option == 4:
            mostrar_inventario()
