# programa para calcular un interes compuesto de una capital C

#entrada
C = int(input( " por favor digite el valor inical de su capital (C) : "))
print ( " su valor inicial fue : ", C )

#proceso y salida
N = 0 
D = 2 * C

while ( C <= D ):
    C = 1.05*C
    N = N+1
print ( " la cantidad de meses son : " + str (N))
print ( "el valor final es de : " + str (C))