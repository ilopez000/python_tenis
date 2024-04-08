import pygame
import sys
import random

# Inicializar Pygame
pygame.init()

# Constantes para la pantalla
ANCHO = 800
ALTO = 600

# Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)

# Configuración de la pantalla
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego de Tenis")

# Variables del juego
velocidad_pelota_x = 7 * random.choice((1, -1))
velocidad_pelota_y = 7 * random.choice((1, -1))
velocidad_jugador = 0
velocidad_oponente = 7

# Rectángulos para la pelota y las raquetas
pelota = pygame.Rect(ANCHO / 2 - 15, ALTO / 2 - 15, 30, 30)
jugador = pygame.Rect(ANCHO - 20, ALTO / 2 - 70, 10, 140)
oponente = pygame.Rect(10, ALTO / 2 - 70, 10, 140)

reloj = pygame.time.Clock()

# Bucle principal del juego
while True:
    # Manejar eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_DOWN:
                velocidad_jugador += 7
            if evento.key == pygame.K_UP:
                velocidad_jugador -= 7
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_DOWN:
                velocidad_jugador -= 7
            if evento.key == pygame.K_UP:
                velocidad_jugador += 7

    # Mover las raquetas
    jugador.y += velocidad_jugador
    if oponente.top < pelota.y:
        oponente.top += velocidad_oponente
    if oponente.bottom > pelota.y:
        oponente.bottom -= velocidad_oponente

    # Mantener las raquetas en pantalla
    if jugador.top <= 0:
        jugador.top = 0
    if jugador.bottom >= ALTO:
        jugador.bottom = ALTO
    if oponente.top <= 0:
        oponente.top = 0
    if oponente.bottom >= ALTO:
        oponente.bottom = ALTO

    # Mover la pelota
    pelota.x += velocidad_pelota_x
    pelota.y += velocidad_pelota_y

    # Colisión de la pelota con las paredes
    if pelota.top <= 0 or pelota.bottom >= ALTO:
        velocidad_pelota_y *= -1
    if pelota.left <= 0 or pelota.right >= ANCHO:
        pelota.center = (ANCHO / 2, ALTO / 2)
        velocidad_pelota_x *= random.choice((1, -1))
        velocidad_pelota_y *= random.choice((1, -1))

    # Colisión de la pelota con las raquetas
    if pelota.colliderect(jugador) or pelota.colliderect(oponente):
        velocidad_pelota_x *= -1

    # Visualización
    pantalla.fill(NEGRO)
    pygame.draw.rect(pantalla, BLANCO, jugador)
    pygame.draw.rect(pantalla, BLANCO, oponente)
    pygame.draw.ellipse(pantalla, BLANCO, pelota)
    pygame.draw.aaline(pantalla, BLANCO, (ANCHO / 2, 0), (ANCHO / 2, ALTO))

    pygame.display.flip()
    reloj.tick(60)
