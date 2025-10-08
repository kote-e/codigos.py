import random

def Crear_tablero(numero):
    """Crea un tablero de juego con el número de filas y columnas especificado."""
    return [[' ' for _ in range(numero)] for _ in range(numero)]

def minas(tablero, numero, primera_fila=None, primera_columna=None):
    """Coloca minas aleatoriamente en el tablero, evitando la primera celda seleccionada."""
    tamano = len(tablero)
    minas = 0
    while minas < numero:
        fila = random.randint(0, tamano - 1)
        columna = random.randint(0, tamano - 1)
        # Evitar colocar mina en la primera celda clickeada y sus alrededores
        if (fila == primera_fila and columna == primera_columna) or tablero[fila][columna] == 'M':
            continue
        if primera_fila is not None and abs(fila - primera_fila) <= 1 and abs(columna - primera_columna) <= 1:
            continue
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
    return ' ' if contador == 0 else str(contador)

def seleccionar_celda(tablero_real, tablero_visible, fila, columna):
    """Revela una celda del tablero. Si no hay minas alrededor, revela en cadena."""
    if tablero_visible[fila][columna] not in [' ', '🚩']:
        return True  # Ya revelada

    if tablero_real[fila][columna] == 'M':
        tablero_visible[fila][columna] = 'M'
        return False

    numero = minas_adyacentes(tablero_real, fila, columna)
    tablero_visible[fila][columna] = numero

    if numero == ' ':
        for i in range(fila - 1, fila + 2):
            for j in range(columna - 1, columna + 2):
                if 0 <= i < len(tablero_real) and 0 <= j < len(tablero_real):
                    if tablero_visible[i][j] == ' ':
                        seleccionar_celda(tablero_real, tablero_visible, i, j)

    return True

def win(tablero_real, tablero_visible):
    """Verifica si el jugador ha ganado."""
    for i in range(len(tablero_real)):
        for j in range(len(tablero_real)):
            if tablero_real[i][j] != 'M' and tablero_visible[i][j] in [' ', '🚩']:
                return False
    return True
    """Verifica si el jugador ha ganado."""
    for i in range(len(tablero_real)):
        for j in range(len(tablero_real)):
            if tablero_real[i][j] != 'M' and tablero_visible[i][j] == ' ':
                return False
    return True