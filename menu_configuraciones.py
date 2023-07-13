import pygame
from funciones import*
from botones import*

class Configuraciones:
    def __init__(self, volumen_lluvia, volumen_musica) -> None:
        self.volumen_lluvia = volumen_lluvia
        self.volumen_musica = volumen_musica
        self.variable_volumen = 0


    def draw(self, pantalla, fuente, menu_de_pausa, fondo, boton_subir, boton_bajar, sonido_click):
        pantalla.blit(fondo,(0,0))  
        pantalla.blit(menu_de_pausa,(50,250))

        draw_texto(pantalla, 'Sonido', fuente, "Black", 260, 360)

        subir_volumen_lluvia = Menu(180,400,boton_subir)
        subir_lluvia = subir_volumen_lluvia.draw(pantalla, sonido_click)
        if subir_lluvia:
            self.volumen_lluvia += 0.1

        bajar_volumen_lluvia = Menu(180,460,boton_bajar)
        bajar_lluvia = bajar_volumen_lluvia.draw(pantalla, sonido_click)
        if bajar_lluvia:
            self.volumen_lluvia -= 0.1
        draw_texto(pantalla, 'Lluvia', fuente, "Black", 165, 430)


        subir_volumen_musica = Menu(280,400,boton_subir)
        subir_musica = subir_volumen_musica.draw(pantalla, sonido_click)
        if subir_musica:
            self.volumen_musica += 0.1
        bajar_volumen_musica = Menu(280,460,boton_bajar)
        bajar_musica = bajar_volumen_musica.draw(pantalla, sonido_click)
        if bajar_musica:
            self.volumen_musica -= 0.1
        draw_texto(pantalla, 'Musica', fuente, "Black", 260, 430)


        subir_volumen_efectos = Menu(380,400,boton_subir)
        subir_efectos = subir_volumen_efectos.draw(pantalla, sonido_click)
        if subir_efectos:
            self.variable_volumen += 0.1

        bajar_volumen_efectos = Menu(380,460,boton_bajar)
        bajar_efectos = bajar_volumen_efectos.draw(pantalla, sonido_click)
        if bajar_efectos:
            self.variable_volumen -= 0.1
        draw_texto(pantalla, 'Efectos', fuente, "Black", 360, 430)

        draw_texto(pantalla, 'Precione "Escape" para volver', fuente, "White", 150, 750)


    def get_volumen_lluvia(self):
        return self.volumen_lluvia
    
    def get_volumen_musica(self):
        return self.volumen_musica
    
    def get_volumen_efectos(self):
        return self.variable_volumen