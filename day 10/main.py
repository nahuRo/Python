import pygame
import random
import math
from pygame import mixer # para sonidos

# inicializo pygame
pygame.init()

# crear pantalla (ancho, largo)
pantalla = pygame.display.set_mode((800, 600))

# titulo e icono
pygame.display.set_caption("Invación Especial") # titulo de la ventana
icono = pygame.image.load("./day 10/ovni.png") # cargo la img
pygame.display.set_icon(icono) # asigno la img a la ventana
fondo = pygame.image.load("./day 10/espacio.png") #
# agregar musica
mixer.music.load("./day 10/MusicaFondo.mp3") 
mixer.music.set_volume(1) # para conf el vol
mixer.music.play(-1) # -1, para que suene cada vez que termine, si no le pongo nada se pone para siempre

# variables jugador
img_player = pygame.image.load("./day 10/nave-espacial.png")
player_x = 368 # (800/2 - 64/2) posicion en el eje x
player_y = 530 # (600 - 64 - (unos px para subirlo un poco )) posicion en el eje y
player_x_cambio = 0 # para ir cambiando la pos x

# variables enemigo
img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 5

for enemigo in range(cantidad_enemigos):
    img_enemigo.append(pygame.image.load("./day 10/enemigo.png"))
    enemigo_x.append(random.randint(0, 736)) # (800/2 - 64/2) posicion en el eje x
    enemigo_y.append(random.randint(50, 200)) # (600 - 64) posicion en el eje y
    enemigo_x_cambio.append(1.5) # para ir cambiando la pos x
    enemigo_y_cambio.append(50)


# variables de la bala
img_bala = pygame.image.load("./day 10/bala.png")
bala_x = 0 
bala_y = 500
bala_y_cambio = 4
visibilidad_bala = False

# variable de puntuacion
puntaje = 0
fuente = pygame.font.Font("freesansbold.ttf", 18)
puntaje_x = 700
puntaje_y = 10

# variable texto final del juego
fuente_final = pygame.font.Font("freesansbold.ttf", 40)


# funcion para setear la posicion del player
def player(x, y):
    pantalla.blit(img_player,(x, y)) # metodo para arrojar/renderizar a nuestro jugador en la pantalla

# funcion para setear la posicion del enemigo
def enemigo(x, y, ene):
    pantalla.blit(img_enemigo[ene],(x, y)) # metodo para arrojar/renderizar a nuestro enemigo en la pantalla

# funcion disparar bala
def disparar_bala(x, y):
    global visibilidad_bala
    visibilidad_bala = True
    pantalla.blit(img_bala,(x + 16, y + 10)) # le agrego esos valores para que la bala arranque del centro de la nave y no de abajo

# funcion para detectar colisiones
def colision(x_1, y_1, x_2, y_2):
    distancia = math.sqrt(math.pow(x_2 - x_1, 2) + math.pow(y_2 - y_1, 2)) 
    if distancia < 27:
        return True
    else:
        return False

# funcion para mostrar puntaje
def mostrar_puntaje(x, y):
    texto = fuente.render(f"Puntaje: {puntaje}", True, (255,255,255))
    pantalla.blit(texto, (x,y))

# funcion para mostrar el cartel de GAME OVER
def texto_final():
    mi_fuente_final = fuente_final.render(f"GAME OVER", True, (255,255,255))
    pantalla.blit(mi_fuente_final, (60, 200))


# loop para que no se cierre la pantalla
se_ejecuta = True
while se_ejecuta:

    # imagen de fondo
    pantalla.blit(fondo,(0, 0))

    # asigno color al fondo de pantalla
    # pantalla.fill((205, 144, 228)) 

    # ciclo por los eventos como son el click, las flechitas, etc
    for event in pygame.event.get():
        # evento QUIT es hacer click en la X para salir
        if event.type == pygame.QUIT:
            se_ejecuta = False

        # evento KEYDOWN se fija si hay una tecla presionada
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_cambio = -2

            if event.key == pygame.K_RIGHT:
                player_x_cambio = 2

            if event.key == pygame.K_SPACE:
                # dandole sonido cuando dispara
                sonido_bala = mixer.Sound("./day 10/disparo.mp3")
                sonido_bala.play()

                if not visibilidad_bala:
                    bala_x = player_x
                    disparar_bala(bala_x, bala_y)
                
        # evento KEYUP se fija cuado se suelta una tecla
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_cambio = 0

    # setear posicion del player
    player_x += player_x_cambio

    # limito posicion dentro de pantalla del player
    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736

    # setear posicion del enemigo
    for e in range(cantidad_enemigos):

        # fin del juego
        if enemigo_y[e] > 500:
            for k in range(cantidad_enemigos):
                enemigo_y[k] = 1000

            texto_final()
            break
        enemigo_x[e] += enemigo_x_cambio[e]

        # limito posicion dentro de pantalla del enemigo
        if enemigo_x[e] <= 0:
            enemigo_x_cambio[e] = 1.5
            enemigo_y[e] += enemigo_y_cambio[e]
        elif enemigo_x[e] >= 736:
            enemigo_x_cambio[e] = -1.5
            enemigo_y[e] += enemigo_y_cambio[e]

        # chequeo de colision 
        hay_colision = colision(enemigo_x[e], enemigo_y[e],bala_x, bala_y)
        if hay_colision:
            sonido_colision = mixer.Sound("./day 10/golpe.mp3")
            sonido_colision.play()
            bala_y = 500
            visibilidad_bala = False
            puntaje += 10
            enemigo_x[e] = random.randint(0, 736)
            enemigo_y[e] = random.randint(50, 200)
            
        enemigo(enemigo_x[e], enemigo_y[e], e)

    # limitacion de pantalla para bala
    if bala_y <= -64:
        bala_y = 500
        visibilidad_bala = False

    # movimiento bala
    if visibilidad_bala:
        disparar_bala(bala_x, bala_y)
        bala_y -= bala_y_cambio

    player(player_x, player_y)
    
    # mostrando puntaje
    mostrar_puntaje(puntaje_x, puntaje_y)

    # actualizo todos los datos en la pantalla, para que se setee el fondo de pantalla
    pygame.display.update()   