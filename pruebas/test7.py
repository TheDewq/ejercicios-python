import math
sombrero = [1,2,3,4,5]
mitad = math.ceil( len(sombrero) /2 );
sombrero[mitad] = int( input( "Ingrese un valor para remplazar el numero de la mitad" ) )
del sombrero[-1]
print(len(sombrero))
