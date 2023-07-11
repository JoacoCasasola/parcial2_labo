import pygame,random
from constantes import*

class Poderes:
    def __init__(self, path) -> None:
        self.imagen = pygame.image.load(path)
        self.imagen = pygame.transform.scale(self.imagen, (40,40))
        self.rect = self.imagen.get_rect()
        self.rect.x = random.randint(0,ANCHO_VENTANA - 20)
        self.rect.y = -50
        
    def update(self, scroll):
        self.rect.y += 5 + scroll
        if self.rect.top >= ALTO_VENTANA:
            self.rect.y = -1000
            self.rect.x = random.randint(20,ANCHO_VENTANA - 20)

    def draw(self,pantalla): 
        pantalla.blit(self.imagen, self.rect)
