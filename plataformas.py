import pygame
from constantes import*

class Plataforma(pygame.sprite.Sprite):
    def __init__(self,x,y,ancho,path) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path).convert_alpha()
        self.image = pygame.transform.scale(self.image,(ancho,20))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self,scroll):
        self.rect.y += scroll
