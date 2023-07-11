import pygame
from animaciones import*
from constantes import*

class EnemigoFinal(pygame.sprite.Sprite):
    def __init__(self,x,y) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.demonioF_quieto_izquierda = enemigo_final_quieto_izquierda
        self.demonioF_ataque_izquierda = enemigo_final_ataque_izquierda

        self.frame = 0
        self.contador_direccion = 0
        self.contador_ataque = 0

        self.animacion = self.demonioF_quieto_izquierda

        self.image = self.animacion[self.frame]
        self.image = pygame.transform.scale(self.image,(90,120))
        self.rect = self.image.get_rect()
        self.rect_coli = pygame.Rect(0,0,50,100)

        self.flip = False
        self.hp = 150
        
        self.rect.x = x
        self.rect.y = y
        self.rect_coli.x = self.rect.centerx - 20
        self.rect_coli.y = self.rect.centery - 40


    def update(self,scroll):
        self.rect.y += scroll
        self.rect_coli.y += scroll
        self.contador_direccion += 1

        if self.contador_direccion >= 100:
            self.flip = True
        elif self.contador_direccion < 100:
            self.flip = False

        if self.contador_direccion >= 200:
            self.contador_direccion = 0


    def anima_enemigo_final(self):
        self.contador_ataque += 1
        if self.frame >= len(self.animacion)-1:
            self.animacion = self.demonioF_quieto_izquierda

        if self.contador_ataque >= 250:
            self.animacion = self.demonioF_ataque_izquierda
        elif self.contador_ataque < 250:
            self.animacion = self.demonioF_quieto_izquierda

        if self.contador_ataque >= 300:
            self.contador_ataque = 0

        if (self.frame < len(self.animacion)-1):
            self.frame += 1
        else:
            self.frame = 0


    def draw(self,pantalla):
        self.image = self.animacion[self.frame]
        self.image = pygame.transform.scale(self.image,(100,130))
        pantalla.blit(pygame.transform.flip(self.image, self.flip, False), (self.rect.x, self.rect.y))
        pygame.draw.rect(pantalla, "Red", (self.rect.x- 10, self.rect.y - 20, 120,10))
        pygame.draw.rect(pantalla, "Violet", (self.rect.x- 10, self.rect.y - 20, 120 - (150-self.hp),10))
        # pygame.draw.rect(pantalla,"Red",self.rect_coli,2)

        