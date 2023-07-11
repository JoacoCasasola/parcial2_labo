import pygame
from animaciones import balas_jugador, balas_demonios

class DisparosEnemigos(pygame.sprite.Sprite):
    def __init__(self, x, y, velocidad):
        pygame.sprite.Sprite.__init__(self)
        self.bala = balas_demonios
        self.animacion = balas_demonios
        self.frame = 0
        self.image = self.animacion[self.frame]
        self.image = pygame.transform.scale(self.image,(30,30))
        self.rect = self.image.get_rect()
        self.rect.x = x + 30
        self.rect.y = y + 80
        self.velocidad = velocidad
        

    def disparo_animacion(self):
        if (self.frame < len(self.animacion)-1):
            self.frame += 1
        else:
            self.frame = 0

    def update(self,scroll):
        self.rect.y += scroll + self.velocidad

    
    def draw(self,pantalla):
        self.image = self.animacion[self.frame]
        self.image = pygame.transform.scale(self.image,(30,30))
        pantalla.blit(self.image,self.rect)
        # pygame.draw.rect(pantalla,"Red",self.rect,2)
        



class DisparosJugador(pygame.sprite.Sprite):
    def __init__(self, x, y, velocidad):
        pygame.sprite.Sprite.__init__(self)
        self.bala = balas_jugador
        self.animacion = balas_jugador
        self.frame = 0
        self.image = self.animacion[self.frame]
        self.image = pygame.transform.scale(self.image,(30,30))
        self.rect = self.image.get_rect()
        self.rect.x = x + 30
        self.rect.y = y + 80
        self.velocidad = velocidad
        
        

    def disparo_animacion(self):
        if (self.frame < len(self.animacion)-1):
            self.frame += 1
        else:
            self.frame = 0

    def update(self):
        self.rect.y -= self.velocidad

    
    def draw(self,pantalla):
        self.image = self.animacion[self.frame]
        self.image = pygame.transform.scale(self.image,(30,30))
        pantalla.blit(self.image,self.rect)
        # pygame.draw.rect(pantalla,"Red",self.rect,2)