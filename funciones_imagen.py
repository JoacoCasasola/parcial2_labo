import pygame
from constantes import*

def draw_texto(pantalla,text,font,color,x,y):
    img = font.render(text,True,color)
    pantalla.blit(img,(x,y))
    return img

def draw_panel(pantalla,fuente,puntos,vida,personaje):
    pygame.draw.rect(pantalla,"Black", (0,0,ANCHO_VENTANA,45))
    pygame.draw.line(pantalla,"White", (0,45),(ANCHO_VENTANA,45),2)
    draw_texto(pantalla,"SCORE: " + str(puntos), fuente, "White",15,7)

    if personaje.hp == 3:
        pantalla.blit(vida,(500,10))
    if personaje.hp >= 2:
        pantalla.blit(vida,(530,10))
    if personaje.hp > 0:
        pantalla.blit(vida,(560,10))

    if puntos >= 10 and puntos <= 70:
        draw_texto(pantalla,"Level 1", fuente,"White",250,7)
    elif puntos >= 70 and puntos <= 150:
        draw_texto(pantalla,"Level 2", fuente,"White",250,7)
    elif puntos >= 150 and puntos <= 250:
        draw_texto(pantalla,"Level 3", fuente,"White",250,7)

    


def draw_fondo(pantalla,fondo,fondo_scroll):
    pantalla.blit(fondo,(0,0 + fondo_scroll))
    pantalla.blit(fondo,(0,-800 + fondo_scroll))
    
    