import pygame
import sys

# Inicializar Pygame
pygame.init()

# Crear ventana (ancho, alto)
pantalla = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Prueba de Pygame")

# Color de fondo (RGB)
color_fondo = (100, 149, 237)  # Azul tipo "Cornflower"

# Bucle principal
while True:
    # Revisar eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:  # Si se cierra la ventana
            pygame.quit()
            sys.exit()

    # Rellenar fondo
    pantalla.fill(color_fondo)

    # Actualizar pantalla
    pygame.display.flip()