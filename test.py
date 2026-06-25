import os
import time
import random
import sys  # <-- 1. Agrega esta librería
import subprocess


sys.stdout.reconfigure(encoding='utf-8')

# --- CONFIGURACIÓN INICIAL ---
FILAS = 5
COLUMNAS = 10
zombies_restantes = 10
# Cada zombie será una lista con 2 valores: [fila, columna]
zombies_en_pantalla = [] 

juego_activo = True

# --- BUCLE PRINCIPAL DEL JUEGO ---
while juego_activo:
    
    # 1. Limpiar la terminal (compatible con Windows, Mac y Linux)
    if os.name == 'nt':
        subprocess.run('cls', shell=True)
    else:
        subprocess.run('clear', shell=True)

    # 2. Aparición (Spawn) de Zombies en la derecha
    if zombies_restantes > 0:
        # Hay un 40% de probabilidad de que aparezca un zombie en este turno
        if random.randint(1, 100) <= 40: 
            fila_aleatoria = random.randint(0, FILAS - 1)
            columna_aparicion = COLUMNAS - 1 # Extremo derecho
            
            # Iteramos para verificar que el lugar de aparición esté vacío
            casilla_ocupada = False
            for z in zombies_en_pantalla:
                if z[0] == fila_aleatoria and z[1] == columna_aparicion:
                    casilla_ocupada = True
            
            # Si nadie ocupa ese lugar, aparece el zombie
            if not casilla_ocupada:
                zombies_en_pantalla.append([fila_aleatoria, columna_aparicion])
                zombies_restantes -= 1

    # 3. Mover a los Zombies mediante iteraciones
    for z in zombies_en_pantalla:
        # Probabilidad del 20% de que el zombie cambie de línea
        if random.randint(1, 100) <= 20: 
            direccion = random.choice([-1, 1]) # -1 (sube una fila), 1 (baja una fila)
            nueva_fila = z[0] + direccion
            
            # Nos aseguramos de que no se salga del tablero por arriba o abajo
            if 0 <= nueva_fila < FILAS:
                # Verificamos que la nueva posición no tenga ya otro zombie
                casilla_ocupada = False
                for otro_z in zombies_en_pantalla:
                    if otro_z[0] == nueva_fila and otro_z[1] == z[1]:
                        casilla_ocupada = True
                
                if not casilla_ocupada:
                    z[0] = nueva_fila # Efectuamos el cambio de línea

        # Mover un paso hacia la izquierda
        z[1] -= 1
        
        # Condición de derrota: Si cruza el límite izquierdo de la matriz
        if z[1] < 0:
            juego_activo = False

    # 4. Dibujar la matriz (Tablero)
    # 4a. Dibujar las coordenadas de las columnas en la parte superior
    print("     ", end="")
    for c in range(COLUMNAS):
        print(f"{c}  ", end="")
    print("\n   " + "-" * (COLUMNAS * 3 + 2))

    # 4b. Dibujar las filas con sus coordenadas y los zombies
    for f in range(FILAS):
        print(f"{f} | ", end="") # Coordenada lateral (número de fila)
        
        for c in range(COLUMNAS):
            # Usamos otra iteración para ver si un zombie coincide con esta coordenada (f, c)
            hay_zombie = False
            for z in zombies_en_pantalla:
                if z[0] == f and z[1] == c:
                    hay_zombie = True
                    break # Si encontramos uno, no hace falta seguir buscando en esta casilla
            
            # Imprimimos el emoji o un punto para casillas vacías
            if hay_zombie:
                print("👽 ", end="")
            else:
                print(" . ", end="")
        
        print() # Salto de línea para pasar a la siguiente fila del tablero
    
    # 5. Información en pantalla
    print("\nZombies esperando para atacar:", zombies_restantes)
    
    if not juego_activo:
        print("¡UN ZOMBIE LLEGÓ A LA IZQUIERDA! GAME OVER 💀")
        break # Rompe el ciclo principal y termina el programa

    # 6. Pausar la ejecución un segundo para que se vea como una animación
    time.sleep(1)