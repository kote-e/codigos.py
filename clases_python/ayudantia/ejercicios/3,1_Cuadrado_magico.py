def es_cuadrado_magico(cuadrado):
    n=len(cuadrado)
    suma_diagonal_principal=0
    suma_diagonal_secundaria=0

    #Calculamos las diagonales
    for i in range (n):
        suma_diagonal_principal+=cuadrado[i][i]
        suma_diagonal_secundaria+=cuadrado[i][n-1-i]
    if suma_diagonal_principal != suma_diagonal_secundaria:
        return False

    #Calculamos las filas y columnas
    for i in range(n):
        suma_fila=0
        suma_columna=0
        for j in range(n):
            suma_fila+=cuadrado[i][j]
            suma_columna+=cuadrado[j][i]
        if suma_fila != suma_diagonal_principal or suma_columna != suma_diagonal_principal:
            return False
        
    return suma_diagonal_principal




ancho=int(input("Ingrese el ancho del cuadrado mágico: "))
Cuadrado=[]
for i in range(ancho):
    fila=[]
    for j in range(ancho):
        numero= int(input(f"Ingrese el número para la posición ({i+1},{j+1}): "))
        fila.append(numero)
    Cuadrado.append(fila)



print( f"El cuadrado mágico ingresado es:" )
for fila in Cuadrado:
    print(fila)

numero= es_cuadrado_magico(Cuadrado)
if numero:
    print(numero)
else:
    print("NO")