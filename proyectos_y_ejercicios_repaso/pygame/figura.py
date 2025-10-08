import pygame
import sys

# Inicializar Pygame
pygame.init()

# Crear ventana
pantalla = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Figuras en Pygame")

# Colores (RGB)
color_fondo = (30, 30, 30)      # Fondo gris oscuro
color_circulo = (255, 0, 0)     # Rojo
color_rectangulo = (0, 255, 0)  # Verde

# Bucle principal
while True:
    # Revisar eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Rellenar fondo
    pantalla.fill(color_fondo)

    # Dibujar un círculo (superficie, color, posición (x,y), radio)
    pygame.draw.circle(pantalla, color_circulo, (150, 200), 50)

    # Dibujar un rectángulo (superficie, color, rectángulo (x, y, ancho, alto))
    pygame.draw.rect(pantalla, color_rectangulo, (350, 150, 100, 100))

    # Actualizar pantalla
    pygame.display.flip()