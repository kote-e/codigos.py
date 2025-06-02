def buscar_minas(tablero):
    """
    Busca minas en el tablero y devuelve una lista de coordenadas donde se encuentran las minas.

    :param tablero: Lista de listas que representa el tablero del juego.
    :return: Lista de tuplas con las coordenadas (fila, columna) de las minas.
    """
    minas = []
    for fila in range(len(tablero)):
        for columna in range(len(tablero[fila])):
            if tablero[fila][columna] == 'M':  # Suponiendo que 'M' representa una mina
                minas.append((fila, columna))
    return minas 
