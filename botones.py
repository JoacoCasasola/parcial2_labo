import pygame

class Menu:
    def __init__(self,x,y,superficie) -> None:
        self.imagen = superficie
        self.rect = self.imagen.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.click = False

        
    def draw(self, pantalla, sonido_click):
        pos_mouse = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos_mouse):
            if pygame.mouse.get_pressed()[0] == 1:
                self.click = True
                sonido_click.play()

        if pygame.mouse.get_pressed()[0] == 0:
            self.click = False

        pantalla.blit(self.imagen,(self.rect.x,self.rect.y))

        return self.click
          
        