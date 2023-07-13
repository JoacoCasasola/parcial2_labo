import pygame
from animaciones import*
from constantes import*

class Enemigos(pygame.sprite.Sprite):
    def __init__(self,x,y,demonio_rojo = False) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.demonio1_vuela_izquierda = demonio1_vuela_izquierda
        self.demonio1_ataque_izquierda = demonio1_ataque_izquierda

        self.demonio2_vuela_izquierda = demonio2_vuela_izquierda
        self.demonio2_ataque_izquierda = demonio2_ataque_izquierda

        self.frame = 0
        self.demonio_rojo = demonio_rojo
        
        if self.demonio_rojo:
            self.animacion = self.demonio2_vuela_izquierda
        else:
            self.animacion = self.demonio1_vuela_izquierda

        self.image = self.animacion[self.frame]
        self.image = pygame.transform.scale(self.image,(100,100))
        self.rect = self.image.get_rect()
        self.rect_coli = pygame.Rect(0,0,30,70)

        self.direccion = -1
        self.flip = False
        
        if self.demonio_rojo:
            self.hp = 50
        else:
            self.hp = 30
        
        self.rect.x = x
        self.rect.y = y
        self.rect_coli.x = self.rect.centerx - 15
        self.rect_coli.y = self.rect.centery - 35
        self.caida = 0

    def update(self,scroll):
        self.caida += scroll*2
        self.rect.x += self.direccion * 3
        self.rect.y += scroll
        self.rect_coli.x += self.direccion * 3
        self.rect_coli.y += scroll

        if self.rect.left < 0:
            self.direccion *= -1
            self.flip = True

        if self.rect.right > ANCHO_VENTANA:
            self.direccion *= -1
            self.flip = False
        
        if self.rect.top > ALTO_VENTANA:
            self.kill()

    def enemigo_muere(self, sonido_muere):
        sonido_muere.play()
        self.kill()
        

    def enemigo_animacion(self,esta_disparando):
        if esta_disparando == True:
            if self.demonio_rojo:
                self.animacion = self.demonio2_ataque_izquierda
            else:
                self.animacion = self.demonio1_ataque_izquierda

        if self.frame >= len(self.animacion)-1:
            if self.demonio_rojo:
                self.animacion = self.demonio2_vuela_izquierda
            else:
                self.animacion = self.demonio1_vuela_izquierda

        if (self.frame < len(self.animacion)-1):
            self.frame += 1
        else:
            self.frame = 0

    def draw(self,pantalla):
        self.image = self.animacion[self.frame]
        self.image = pygame.transform.scale(self.image,(90,90))
        pantalla.blit(pygame.transform.flip(self.image, self.flip, False), (self.rect.x, self.rect.y))
        pygame.draw.rect(pantalla, "Red", (self.rect.x, self.rect.y - 20, 60,10))
        pygame.draw.rect(pantalla, (103, 149, 47) , (self.rect.x, self.rect.y - 20, 60 - (2*(30-self.hp)),10))
        # pygame.draw.rect(pantalla,"Blue",self.rect_coli,2)
        
