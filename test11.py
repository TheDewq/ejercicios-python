#programa de inventarios con diccionarios y listas

global inventario
inventario = []

def ver_productos():
	print(inventario)

def agregar_producto(nombre, precio, cantidad, caracteristicas): #IN (nombre:Str precio:int cantidad:int caracteristicas:conjunto) OUT()
	inventario.append({nombre : [precio, cantidad, caracteristicas]})
def ingresar_caracteristicas(): #IN() OUT(conjunto)
	while True:
		x = set({})
		x.add((input("ingresa el nombre de la caracteristica: "), input("ingresa la descripcion de la caracteristica: ")))
		if(int(input("desea Ingresar mas? ( 1 ) = SI ( 2 ) = NO:  ")) == 2):
			break
	return x

def menu(): #IN() OUT()
	while True:
		print("selecciona una opcion")
		print("1] ver productos en stock")
		print("2] agregar prodcuto")
		x = input("= ")
		if x.isnumeric():
			x = int(x)
			if x == 1:
				ver_productos()
				
				continue
			if x == 2:
				agregar_producto(input("ingresa el nombre: "), input("ingresa el precio: "), input("ingresa la cantidad: "), ingresar_caracteristicas())
				continue
		print("no es valida la entrada")	

print("Bienvenido a la tienda re xd")
menu()





