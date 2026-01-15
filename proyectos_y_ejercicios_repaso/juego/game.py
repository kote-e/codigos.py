import pygame
pygame.init() # Inicializa todos los módulos de Pygame
import sys    # Importa el módulo sys para cerrar el programa


# Configuración de la ventana
ANCHO, ALTO = 800, 600
PANTALLA = pygame.display.set_mode((ANCHO, ALTO)) # Crea la ventana del juego
pygame.display.set_caption("Cafetería")
reloj = pygame.time.Clock() # Reloj para controlar los FPS


#fondo = pygame.image.load("imagenes\ChatGPT Image 14 ene 2026, 20_39_25.png").convert() # Carga la imagen de fondo
#fondo = pygame.transform.scale(fondo, (ANCHO, ALTO)) # Escala la imagen al tamaño de la ventana



# imagenes
fondo = pygame.image.load(r"imagenes\Fondo.png").convert() # Carga la imagen de fondo
fondo = pygame.transform.scale(fondo, (ANCHO, ALTO)) # Escala la imagen al tamaño de la ventana

cafe= pygame.image.load("imagenes/cafe.png").convert_alpha() # Carga la imagen de la taza de café
tazacafe= pygame.image.load("imagenes/Tazacafe.png").convert_alpha() # Carga la imagen de la taza con café
taza= pygame.image.load("imagenes/Tazavacia.png").convert_alpha() # Carga la imagen de la taza
cosas = pygame.image.load("imagenes/cosas.png").convert_alpha() # Carga la imagen de cosas
cafelindo= pygame.image.load("imagenes/cafelindo.png").convert_alpha() # Carga la imagen de café lindo
leche= pygame.image.load("imagenes/leche.png").convert_alpha() # Carga la imagen de leche

# sonas clickables 
zona_cafetera = pygame.Rect(40, 300, 260, 200)
zona_tazas = pygame.Rect(200, 260, 160, 120)
zona_mesa = pygame.Rect(
    ANCHO // 2 - taza.get_width() // 2,
    380,  # ajusta este valor mirando el fondo
    taza.get_width(),
    taza.get_height()
)


# 0 = no hay taza
# 1 = taza vacía
# 2 = taza con café
estado_taza = 0

# Bucle principal del juego
ejecutando = True
while ejecutando:

    # Recorremos todos los eventos
    for evento in pygame.event.get():

        # Cerrar la ventana con la X
        if evento.type == pygame.QUIT:
            ejecutando = False

        # Detectar click izquierdo del mouse
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            mouse_pos = evento.pos  # Posición del click

            # Tomar taza vacía
            if zona_tazas.collidepoint(mouse_pos) and estado_taza == 0:
                estado_taza = 1
                print("Taza vacía tomada")

            # Llenar taza con café
            elif zona_cafetera.collidepoint(mouse_pos) and estado_taza == 1:
                estado_taza = 2
                print("Taza con café lista")

            # Entregar café
            elif zona_mesa.collidepoint(mouse_pos) and estado_taza == 2:
                estado_taza = 0
                print("Café entregado ☕")

    # -------- DIBUJO --------
    PANTALLA.blit(fondo, (0, 0))  # Fondo


    # Dibujar taza según estado
    if estado_taza == 1:
        PANTALLA.blit(taza, zona_mesa.topleft)
    elif estado_taza == 2:
        PANTALLA.blit(tazacafe, zona_mesa.topleft)

    pygame.display.flip()  # Actualiza pantalla
    reloj.tick(60)         # 60 FPS

pygame.quit()
sys.exit()