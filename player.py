import pygame
from constantes import*
from enemigos import*
from animaciones import*
from disparos import*

class Player(Enemigos):
    def __init__(self,x,y) -> None:
        self.quieto_derecha = personaje_quieto_derecha
        self.quieto_izquierda = personaje_quieto_izquierda
        self.camina_derecha = personaje_camina_derecha
        self.camina_izquierda = personaje_camina_izquierda
        self.salta_derecha = personaje_salta_derecha
        self.salta_izquierda = personaje_salta_izquierda

        self.frame = 0
        self.velocidad = 10
        self.hp = 3

        self.flip = False
        self.jump = 20

        self.delta_x = 0
        self.delta_y = 0

        self.animacion = self.quieto_derecha
        self.direccion = DIRECCION_DERECHA
        self.image = self.animacion[self.frame]
        self.image = pygame.transform.scale(self.image,(50,70))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.vel_y = 0
        self.esta_saltando = False
        self.esta_muerto = False
        self.sobre_plataforma = False
        self.cantidad_saltos = 0

        self.vidas = 3

        
        
    def mover(self, grupo_plataformas):
        scroll = 0
        self.sobre_plataforma = False
        self.delta_y = self.vel_y    
        self.vel_y += GRAVEDAD

        if self.rect.left + self.delta_x < 0:
            self.delta_x = -self.rect.left
        if self.rect.right + self.delta_x > ANCHO_VENTANA:
            self.delta_x = ANCHO_VENTANA - self.rect.right

        if not self.esta_muerto:
            for plataforma in grupo_plataformas:
                if plataforma.rect.colliderect(self.rect.x, self.rect.y + 10, self.rect.width, self.rect.height):
                    if self.rect.bottom < plataforma.rect.centery:
                        if self.vel_y > 0:
                            self.rect.bottom = plataforma.rect.top
                            self.esta_saltando = False
                            self.delta_y = 0
                    if self.rect.bottom == plataforma.rect.top:
                        self.sobre_plataforma = True
                        self.cantidad_saltos = 0        
            
                      
        if self.rect.top <= 500:
            if self.vel_y < 0:
                scroll = -self.delta_y

        self.rect.x += self.delta_x
        self.rect.y += self.delta_y + scroll
        
        return scroll

    def camina(self, direccion):
        if not self.esta_muerto:
            self.direccion = direccion
            if direccion == DIRECCION_DERECHA:
                self.animacion = personaje_camina_derecha
                self.delta_x += self.velocidad
            else:
                self.animacion = personaje_camina_izquierda
                self.delta_x += -self.velocidad
            self.frame = 0
    
    def salta(self):
        if not self.esta_muerto:
            if self.esta_saltando == False:
                if self.direccion == DIRECCION_DERECHA:
                    self.animacion = personaje_salta_derecha
                else:
                    self.animacion = personaje_salta_izquierda
                self.esta_saltando = True
                self.vel_y = -self.jump
                self.frame = 0  
                
            
    def quieto(self):
        if not self.esta_muerto:
            if self.direccion == DIRECCION_DERECHA:
                self.animacion = personaje_quieto_derecha
            else:
                self.animacion = personaje_quieto_izquierda
            self.delta_x = 0
            self.delta_y = 0
            self.frame = 0

    def ataca(self):
        if not self.esta_muerto:
            if self.direccion == DIRECCION_DERECHA:
                self.animacion = personaje_ataca_derecha
            else:
                self.animacion = personaje_ataca_izquierda
            self.frame = 0
            


    def muere(self,sonido_muere):     
        if self.direccion == DIRECCION_DERECHA:
            self.animacion = personaje_muere_izquierda
            self.delta_x = -4
        else:
            self.animacion = personaje_muere_derecha
            self.delta_x = 4
        self.frame = 0
        self.esta_muerto = True
        sonido_muere.play()
        
    
    
    def personaje_animacion(self):

        if (self.frame < len(self.animacion)-1):
            self.frame += 1
        else:
            self.frame = 0

    def draw(self,pantalla):
        self.image = self.animacion[self.frame]
        pantalla.blit(pygame.transform.flip(self.image, self.flip, False), (self.rect.x, self.rect.y))
        # pygame.draw.rect(pantalla, "Red", (self.rect.x- 10, self.rect.y - 20, 60,5))
        # pygame.draw.rect(pantalla, (54, 124, 220), (self.rect.x- 10, self.rect.y - 20, 60 - (20*(3-self.hp)),5))
        # pygame.draw.rect(pantalla,"Red",self.rect,2)
        