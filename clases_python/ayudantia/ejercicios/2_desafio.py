N= int(input("Ingrese el tamaño de la matriz: "))
posicion_x= int(input("Ingrese la posición x: "))
posicion_y= int(input("Ingrese la posición y: "))
rango= int(input("Ingrese el rango: "))
obstaculos= {(3, 5), (1, 3)}


while True:

    tablero = []
    for i in range(N):
        fila = []
        for j in range(N):
            if i == posicion_x and j == posicion_y:
                fila.append("J")
            elif (i, j) in obstaculos:
                fila.append("X")
            elif (i in range(posicion_x - rango, posicion_x + rango + 1) and j == posicion_y) or (j in range(posicion_y - rango, posicion_y + rango + 1) and i == posicion_x):
                if (i, j) not in obstaculos:
                    fila.append("*")
            else:
                fila.append(".")
        tablero.append(fila)

    for fila in tablero:
        for elemento in fila:
            print(f"{[elemento]}", end=" ")
        print()


    print(f"controles: \n -W arriba \n -S a abajo \n -A a la izquierda \n -D a la derecha \n -Q salir")
    accion= input("Ingrese la acción: ").strip().lower()

    if accion == "q":
        print("Saliendo del programa...")
        break
    nueva_x, nueva_y = posicion_x, posicion_y
    if accion == "w":
        nueva_x -= 1
    elif accion == "s":
        nueva_x += 1
    elif accion == "a":
        nueva_y -= 1
    elif accion == "d":
        nueva_y += 1
    else:
        print("Acción no válida. Intente nuevamente.")
        continue

    if 0 <= nueva_x < N and 0 <= nueva_y < N and (nueva_x, nueva_y) not in obstaculos:
        posicion_x, posicion_y = nueva_x, nueva_y
    elif (nueva_x, nueva_y) in obstaculos:
        print("¡Choque! Hay un obstáculo en esa casilla.")
    else:
        print("Movimiento fuera de los límites del tablero. Intente nuevamente.")
    print("-" * 20)
