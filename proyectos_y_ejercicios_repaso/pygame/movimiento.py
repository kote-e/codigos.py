import pygame
import sys

# Inicializar Pygame
pygame.init()

# Crear ventana
pantalla = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Círculo Movible")

# Colores
color_fondo = (30, 30, 30)
color_circulo = (255, 0, 0)

# Posición inicial del círculo
x = 300
y = 200
radio = 30
velocidad = 5  # Cuántos píxeles se mueve por paso

# Reloj para controlar FPS
reloj = pygame.time.Clock()

# Bucle principal
while True:
    # Limitar a 30 frames por segundo
    reloj.tick(30)  # Más bajo = más lento, más alto = más rápido

    # Revisar eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Detectar teclas presionadas
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        x -= velocidad
    if teclas[pygame.K_RIGHT]:
        x += velocidad
    if teclas[pygame.K_UP]:
        y -= velocidad
    if teclas[pygame.K_DOWN]:
        y += velocidad

    # Limpiar pantalla
    pantalla.fill(color_fondo)

    # Dibujar círculo
    pygame.draw.circle(pantalla, color_circulo, (x, y), radio)

    # Actualizar pantalla
    pygame.display.flip()