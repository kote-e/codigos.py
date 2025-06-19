def Crear_tablero(numero):
    """Crea un tablero de juego con el número de filas y columnas especificado."""
    return [[' ' for _ in range(numero)] for _ in range(numero)]

def minas(tablero, numero):
    """Coloca minas aleatoriamente en el tablero."""
    import random
    tamano = len(tablero)
    minas= 0
    while minas < numero:
        fila = random.randint(0, tamano - 1)
        columna = random.randint(0, tamano - 1)
        if tablero[fila][columna] != 'M':
            tablero[fila][columna] = 'M'
            minas += 1
    return tablero
  
def minas_adyacentes(tablero, fila, columna):
    """Cuenta las minas adyacentes a una celda específica."""
    contador = 0
    for i in range(fila - 1, fila + 2):
        for j in range(columna - 1, columna + 2):
            if 0 <= i < len(tablero) and 0 <= j < len(tablero):
                if tablero[i][j] == 'M':
                    contador += 1
    return str(contador)

def mostrar_tablero(tablero):
    """Muestra el tablero de juego."""
    tamano = len(tablero)
    encabezado = "  " + " ".join(f"{i+1:>2}" for i in range(tamano))
    print(encabezado)
    for i in range(tamano):
        fila_str = f"{i+1:<2} "
        for celda in tablero[i]:
            if celda == ' ':
                fila_str += "[] "
            elif celda == '*':
                fila_str += "*  "
            else:
                fila_str += f"{celda}  "
        print(fila_str)

    return tablero

def seleccionar_celda(tablero_real, tablero_visible, fila, columna):
    """Revela una celda del tablero."""
    if tablero_real[fila][columna] == 'M':
        tablero_visible[fila][columna] = 'M'
        return False
    else:
        numero = minas_adyacentes(tablero_real, fila, columna)
        tablero_visible[fila][columna] = numero
        return True


def win(tablero_visible):
    """Verifica si el jugador ha ganado."""
    for fila in tablero_visible:
        if ' ' in fila:
            return False
    return True

'''programa principal'''
tamano = int(input("Ingrese el tamaño del tablero: "))
numero_minas = int(input("Ingrese el número de minas: "))

tablero = Crear_tablero(tamano)
tablero_visible = Crear_tablero(tamano)
tablero = minas(tablero, numero_minas) 
gano = False

while not gano:
    mostrar_tablero(tablero_visible)

    fila = int(input("Fila: ")) - 1
    columna = int(input("Columna: ")) - 1
    accion = input("Acción (r para revelar, f para bandera): ")
    if accion == 'r':
        if not seleccionar_celda(tablero, tablero_visible, fila, columna):
            print("¡Pisaste una mina! Perdiste.")
            break
        else:
            tablero_visible[fila][columna] = minas_adyacentes(tablero, fila, columna)
    elif accion == 'f':
        if tablero_visible[fila][columna] == '*':
            tablero_visible[fila][columna] = ' '
        else:
            tablero_visible[fila][columna] = '*'
    else:
        print("Acción no válida. Intente de nuevo.")

    if win(tablero_visible):
        print("¡Felicidades, ganaste!")
        break