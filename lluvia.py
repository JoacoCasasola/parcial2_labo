import pygame, random
from constantes import*

class Lluvia:
    def __init__(self) -> None:  
        self.cantidad_gotas = 120  
        self.gota_velocidad = 10  
        self.gota_ancho = 1 
        self.gota_alto = 6  
        self.gota_color = (64, 124, 177)
        self.lista_gotas = []  

    def crea_gotas(self):
        self.lista_gotas = []
        for _ in range(self.cantidad_gotas):
            x = random.randint(0, ANCHO_VENTANA)
            y = random.randint(0, ALTO_VENTANA)
            self.lista_gotas.append([x, y])

    def draw_gotas(self,pantalla,scroll):
        for i in range(self.cantidad_gotas):
            pygame.draw.rect(pantalla, self.gota_color, (self.lista_gotas[i][0], self.lista_gotas[i][1], self.gota_ancho, self.gota_alto))
            self.lista_gotas[i][1] += self.gota_velocidad + scroll
            
            if self.lista_gotas[i][1] > ALTO_VENTANA:
                self.lista_gotas[i][1] = random.randint(-50, -10)
                self.lista_gotas[i][0] = random.randint(0, ANCHO_VENTANA)