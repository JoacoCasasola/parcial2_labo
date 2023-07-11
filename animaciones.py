import pygame
from constantes import *


def gira_imagenes(lista, flip_x, flip_y):
    lista_girada = []
    for imagen in lista:
        lista_girada.append(pygame.transform.flip(imagen, flip_x, flip_y))
    return lista_girada

def reescalar_imagen(lista_animaciones,W,H):
    for lista in lista_animaciones:
        for i in range(len(lista)):
            imagen = lista[i]
            lista[i] = pygame.transform.scale(imagen, (W, H))


demonio_rojo = False

#Player
personaje_quieto_derecha = []
for i in range(1,12):
    personaje_quieto_derecha.append(pygame.image.load(f"recursos\\personaje1\\quieto\\quieto{i}.png"))
personaje_quieto_izquierda = gira_imagenes(personaje_quieto_derecha,True,False)

personaje_camina_derecha = []
for i in range(1,9):
    personaje_camina_derecha.append(pygame.image.load(f"recursos\\personaje1\\camina\\camina{i}.png"))
personaje_camina_izquierda = gira_imagenes(personaje_camina_derecha,True,False)

personaje_ataca_derecha = []
for i in range(1,17):
    personaje_ataca_derecha.append(pygame.image.load(f"recursos\\personaje1\\ataque\\ataque_{i}.png"))
personaje_ataca_izquierda = gira_imagenes(personaje_ataca_derecha,True,False)

personaje_salta_derecha = []
for i in range(1,10):
    personaje_salta_derecha.append(pygame.image.load(f"recursos\\personaje1\\salta\\salto{i}.png"))
personaje_salta_izquierda = gira_imagenes(personaje_salta_derecha,True,False)

personaje_muere_izquierda = []
for i in range(1,15):
    personaje_muere_izquierda.append(pygame.image.load(f"recursos\\personaje1\\muere\\muere{i}.png"))
personaje_muere_derecha = gira_imagenes(personaje_muere_izquierda,True,False)



#Enemigo - demonio1
demonio1_vuela_izquierda = []
for i in range(1,10):
    if demonio_rojo:
        demonio1_vuela_izquierda.append(pygame.image.load(f"recursos\\enemigos\\demonio2.png\\vuela\\vuela{i}.png"))
    else:    
        demonio1_vuela_izquierda.append(pygame.image.load(f"recursos\\enemigos\\demonio1.png\\vuela\\vuela{i}.png"))
demonio1_vuela_derecha = gira_imagenes(demonio1_vuela_izquierda,True,False)

demonio1_ataque_izquierda = []
for i in range(1,16):
    if demonio_rojo:
        demonio1_ataque_izquierda.append(pygame.image.load(f"recursos\\enemigos\\demonio2.png\\ataque\\ataque{i}.png"))
    else:    
        demonio1_ataque_izquierda.append(pygame.image.load(f"recursos\\enemigos\\demonio1.png\\ataque\\ataque{i}.png"))
demonio1_ataque_derecha = gira_imagenes(demonio1_ataque_izquierda,True,False)




#Enemigo Final
enemigo_final_quieto_izquierda = []
for i in range(1,11):
    enemigo_final_quieto_izquierda.append(pygame.image.load(f"recursos\\enemigos\\demonio_Final.png\\quieto\\quieto{i}.png"))
enemigo_final_quieto_derecha = gira_imagenes(enemigo_final_quieto_izquierda,True,False)

enemigo_final_ataque_izquierda = []
for i in range(1,10):
    enemigo_final_ataque_izquierda.append(pygame.image.load(f"recursos\\enemigos\\demonio_Final.png\\ataque\\ataque{i}.png"))
enemigo_final_ataque_derecha = gira_imagenes(enemigo_final_ataque_izquierda,True,False)



#Balas - Demonios
balas_demonios = []
for i in range(1,10):
    balas_demonios.append(pygame.image.load(f"recursos\\enemigos\\demonio1.png\\balas\\bala{i}.png"))

#Balas - jugador
balas_jugador = []
for i in range(1,10):
    balas_jugador.append(pygame.image.load(f"recursos\\personaje1\\disparo\\bala{i}.png"))
