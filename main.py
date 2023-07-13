import pygame, random, os
from constantes import*
from player import*
from enemigos import*
from enemigo_final import*
from disparos import*
from plataformas import*
from funciones import*
from lluvia import*
from botones import*
from poderes import*
from menu_configuraciones import*

pygame.init()


scroll = 0
fondo_scroll = 0
fin_juego = False
in_menu = True
puntos = 0
pantalla_fin_juego = 0
vidas = 3
poder_activado = False
inmunidad = False
cantidad_disparos = 0


inicio = False
in_configuraciones = False
pausa = False
in_tutorial = False
in_opciones = False

cantidad_gotas = 120  
gota_velocidad = 10  
gota_ancho = 1 
gota_alto = 6  
gota_color = (30, 90, 150)  

alpha = 0


if os.path.exists("score.txt"):
    with open("score.txt", "r") as file:
        mejor_punto = str(file.read())
else:
    mejor_punto = 0

fuente1 = pygame.font.SysFont("Garamond", 25)
fuente2 = pygame.font.SysFont("Felix Titling", 60)

pantalla = pygame.display.set_mode(TAMAÑO_VENTANA) 
pygame.display.set_caption("Tp Juego")

tiempo = pygame.time.Clock()

fondo1 = pygame.image.load("recursos\\fondo\\fondo1.jpg").convert_alpha()
fondo1 = pygame.transform.scale(fondo1, TAMAÑO_VENTANA)

fondo2 = pygame.image.load("recursos\\fondo\\fondo4.png").convert_alpha()
fondo2 = pygame.transform.scale(fondo2, TAMAÑO_VENTANA)

fondo3 = pygame.image.load("recursos\\fondo\\fondo3.png").convert_alpha()
fondo3 = pygame.transform.scale(fondo3, TAMAÑO_VENTANA)

fondo_pausa = pygame.image.load("recursos\\fondo\\fondo_pausa.png").convert_alpha()
fondo_pausa = pygame.transform.scale(fondo_pausa, TAMAÑO_VENTANA)

boton_1 = pygame.image.load("recursos\\botones\\boton_menu1.png").convert_alpha()
boton_1 = pygame.transform.scale(boton_1, (200,50))

menu_de_pausa = pygame.image.load("recursos\\botones\\menu1.png").convert_alpha()
menu_de_pausa = pygame.transform.scale(menu_de_pausa,(500,300))

boton_de_pausa = pygame.image.load("recursos\\botones\\boton_pausa.jpg").convert_alpha()
boton_de_pausa = pygame.transform.scale(boton_de_pausa, (30,30))

boton_de_conficuracion = pygame.image.load("recursos\\botones\\boton_ajustes.jpg").convert_alpha()
boton_de_conficuracion = pygame.transform.scale(boton_de_conficuracion, (50,50))

boton_de_salir = pygame.image.load("recursos\\botones\\boton_salir.jpg").convert_alpha()
boton_de_salir = pygame.transform.scale(boton_de_salir, (50,50))

boton_de_reanudar = pygame.image.load("recursos\\botones\\boton_reanudar.jpg").convert_alpha()
boton_de_reanudar = pygame.transform.scale(boton_de_reanudar, (50,50))

boton_bajar_volumen = pygame.image.load("recursos\\botones\\boton_bajar_volumen.jpg")
boton_bajar_volumen = pygame.transform.scale(boton_bajar_volumen,(30,30))

boton_subir_volumen = pygame.image.load("recursos\\botones\\boton_subir_volumen.jpg")
boton_subir_volumen = pygame.transform.scale(boton_subir_volumen,(30,30))



imagen_salto_tuto = pygame.image.load("recursos\\tutorial\\Captura salta.png").convert_alpha()
imagen_salto_tuto = pygame.transform.scale(imagen_salto_tuto, (80,100))

imagen_camina_tuto = pygame.image.load("recursos\\tutorial\\Captura camina.png").convert_alpha()
imagen_camina_tuto = pygame.transform.scale(imagen_camina_tuto, (80,100))

imagen_camina_iz_tuto = pygame.transform.flip(pygame.image.load("recursos\\tutorial\\Captura camina.png").convert_alpha(), True,False)
imagen_camina_iz_tuto = pygame.transform.scale(imagen_camina_iz_tuto, (80,100))

imagen_poder_tuto = pygame.image.load("recursos\\tutorial\\Captura poder.png").convert_alpha()
imagen_poder_tuto = pygame.transform.scale(imagen_poder_tuto, (80,100))

vida = pygame.image.load("recursos\\personaje1\\vidas\\vida1.png").convert_alpha()
vida = pygame.transform.scale(vida, (25,25))

bala = pygame.image.load("recursos\\personaje1\\disparo\\bala4.png").convert_alpha()
bala = pygame.transform.scale(bala, (25,25))



personaje = Player(ANCHO_VENTANA-300,ALTO_VENTANA-150)

disparos_enemigos = DisparosEnemigos(0,0,0)
enemigo_disparando = False

enemigo1 = Enemigos(0, 0)
enemigo2 = Enemigos(0, 0)
enemigo3 = Enemigos(0, 0)

enemigo_final = EnemigoFinal(ANCHO_VENTANA/2-45, 0)
enemigo_final_disparando = False

grupo_plataformas = pygame.sprite.Group()
grupo_enemigos = pygame.sprite.Group()
grupo_disparos_enemigos = pygame.sprite.Group()
grupo_disparos_enemigo_final = pygame.sprite.Group()
grupo_disparos_jugador = pygame.sprite.Group()

plataforma = Plataforma(ANCHO_VENTANA-350,ALTO_VENTANA-50,130,"recursos\\plataforma\\plataforma3.png")
grupo_plataformas.add(plataforma)

lista_rect_enemigos = []
lista_rect_disparos = []
lista_rect_disparos_jugador = []
lista_rect_disparos_enemigo_final = []

sonido_lluvia = pygame.mixer.Sound("recursos\\sonidos\\lluvia.mp3")
musica_fondo = pygame.mixer.Sound("recursos\\sonidos\\medieval.mp3")
musica_victoria = pygame.mixer.Sound("recursos\\sonidos\\musica_victoria2.mp3")
sonido_disparo_enemigo = pygame.mixer.Sound("recursos\\sonidos\\disparos.mp3")
sonido_disparo_jugador = pygame.mixer.Sound("recursos\\sonidos\\disparo_jugador.mp3")
sonido_muere = pygame.mixer.Sound("recursos\\sonidos\\muere.mp3")
sonido_muere2 = pygame.mixer.Sound("recursos\\sonidos\\muere2.mp3")
sonido_muere_enemigo = pygame.mixer.Sound("recursos\\sonidos\\muere_enemigo2.mp3")
sonido_recarga_poder = pygame.mixer.Sound("recursos\\sonidos\\recarga_poder.mp3")
sonido_click = pygame.mixer.Sound("recursos\\sonidos\\sonido_click.mp3")
sonido_resta_vida = pygame.mixer.Sound("recursos\\sonidos\\resta_vida.mp3")
sonido_recarga_vida = pygame.mixer.Sound("recursos\\sonidos\\recarga_vida.mp3")
sonido_risa_enemigo = pygame.mixer.Sound("recursos\\sonidos\\risa_enemigo.mp3")

musica_fondo.play(-1)

sonido_lluvia.play(-1)



menu_configuraciones = Configuraciones(1, 0.15)


lluvia = Lluvia()
lluvia.crea_gotas()

elixir_poder = Poderes("recursos\\poderes\\elixir1.png")
elixir_vida = Poderes("recursos\\poderes\\elixir_vida.png")



run = True
while run:
    

    volumen_lluvia = menu_configuraciones.get_volumen_lluvia()
    volumen_musica = menu_configuraciones.get_volumen_musica()
    variable_volumen = menu_configuraciones.get_volumen_efectos()

    volumen_disparo_enemigo = 0.2 + variable_volumen
    volumen_disparo_jugador = 1 + variable_volumen
    volumen_muere = 0.2 + variable_volumen
    volumen_muere2 = 0.5 + variable_volumen
    volumen_muere_enemigo = 0.2 + variable_volumen
    volumen_recarga_poder = 0.2 + variable_volumen
    volumen_click = 1 + variable_volumen
    volumen_resta_vida = 0.5 + variable_volumen
    volumen_recarga_vida = 0.5 + variable_volumen
    volumen_risa_enemigo = 0.5 + variable_volumen
    volumen_musica_victoria = 0.5 + variable_volumen

    sonido_lluvia.set_volume(volumen_lluvia)#1
    musica_fondo.set_volume(volumen_musica)#0.15
    sonido_disparo_enemigo.set_volume(volumen_disparo_enemigo)#0.2
    sonido_disparo_jugador.set_volume(volumen_disparo_jugador)#0.2
    sonido_muere.set_volume(volumen_muere)#0.2
    sonido_muere2.set_volume(volumen_muere2)#0.5
    sonido_muere_enemigo.set_volume(volumen_muere_enemigo)#0.2
    sonido_recarga_poder.set_volume(volumen_recarga_poder)#0.2
    sonido_click.set_volume(volumen_click)#1
    sonido_resta_vida.set_volume(volumen_resta_vida)#0.5
    sonido_recarga_vida.set_volume(volumen_recarga_vida)#0.5
    sonido_risa_enemigo.set_volume(volumen_risa_enemigo)
    musica_victoria.set_volume(volumen_musica_victoria)



    tiempo.tick(FPS)
    cronometro = int(pygame.time.get_ticks()/1000)

    if in_menu:

        pantalla.blit(fondo3,(0,0))  
    
        boton_inicio = Menu(200,340,boton_1)
        if boton_inicio.draw(pantalla, sonido_click):
            inicio = True

        boton_opciones= Menu(200,410,boton_1)
        if boton_opciones.draw(pantalla, sonido_click):
            in_opciones = True

        boton_tutorial = Menu(200,480,boton_1)
        if boton_tutorial.draw(pantalla, sonido_click):
            in_tutorial = True

        draw_texto(pantalla, "Inicio", fuente1, "Black", 270, 350)
        draw_texto(pantalla, "Opciones", fuente1, "Black", 255, 420)
        draw_texto(pantalla, "Tutorial", fuente1, "Black", 260,490)

        if inicio:
            in_menu = False

        elif in_tutorial:
            inicio = False
            in_opciones = False

            pantalla.fill("Black")  
            pantalla.blit(imagen_salto_tuto, (250,130))
            pantalla.blit(imagen_camina_tuto, (100,280))
            pantalla.blit(imagen_poder_tuto, (250,400))
            pantalla.blit(imagen_camina_iz_tuto, (400,280))
            draw_texto(pantalla, 'Tutorial', fuente2, "White", 150, 20)
            draw_texto(pantalla, '"↑"', fuente1, "White", 270, 240)
            draw_texto(pantalla, '"→"', fuente1, "White", 420,390)
            draw_texto(pantalla, '"←"', fuente1, "White",120, 390)
            draw_texto(pantalla, '"Espacio"', fuente1, "White", 245,520)

            pantalla.blit(elixir_vida.imagen, (180,600))
            pantalla.blit(elixir_poder.imagen, (380,600))
            draw_texto(pantalla, 'Elixir de vida', fuente1, "White", 135, 640)
            draw_texto(pantalla, 'Elixir de poder', fuente1, "White", 330, 640)
            draw_texto(pantalla, 'Precione "Escape" para volver', fuente1, "White", 150, 750)

        elif in_opciones:
            inicio = False
            in_tutorial = False
            menu_configuraciones.draw(pantalla, fuente1, menu_de_pausa, fondo2, boton_subir_volumen, boton_bajar_volumen,sonido_click)


    if fin_juego == False and in_menu == False:
       
        scroll = personaje.mover(grupo_plataformas)

        personaje.personaje_animacion()
        enemigo_final.anima_enemigo_final()
        enemigo1.enemigo_animacion(enemigo_disparando)
        enemigo2.enemigo_animacion(enemigo_disparando)
        enemigo3.enemigo_animacion(enemigo_disparando)
        

        fondo_scroll += scroll  
        if fondo_scroll >= 800:
            fondo_scroll = 0
        

        draw_fondo(pantalla, fondo1, fondo_scroll)


        if scroll > 0:
            puntos += int(scroll/10)


        if len(grupo_plataformas) < MAX_PLATAFORMAS:
            p_w = random.randint(40,90)
            p_x = random.randint(0, ANCHO_VENTANA - p_w)
            p_y = plataforma.rect.y - random.randint(80, 120) 
            plataforma = Plataforma(p_x, p_y, p_w,"recursos\\plataforma\\plataforma3.png")
            grupo_plataformas.add(plataforma)
        grupo_plataformas.update(scroll)
        grupo_plataformas.draw(pantalla)

        if puntos >= 25 and puntos <= 190 and len(grupo_enemigos) == 0:
            enemigo1 = Enemigos(0, 0)
            rect_coli_enemigo1 = enemigo1.rect_coli
            enemigo2 = Enemigos(250, 90)
            rect_coli_enemigo2 = enemigo2.rect_coli
            enemigo3 = Enemigos(500, 180)
            rect_coli_enemigo3 = enemigo3.rect_coli
            lista_rect_enemigos.append(rect_coli_enemigo1)
            lista_rect_enemigos.append(rect_coli_enemigo2)
            lista_rect_enemigos.append(rect_coli_enemigo3)
            grupo_enemigos.add(enemigo1)
            grupo_enemigos.add(enemigo2)
            grupo_enemigos.add(enemigo3)
        grupo_enemigos.update(scroll)


        # Colision de los enemigos - Vidas
        colision_enemigo1 = pygame.sprite.spritecollide(enemigo1, grupo_disparos_jugador, True)
        if colision_enemigo1:
            enemigo1.hp -= 10
            if enemigo1.hp <= 0:
                enemigo1.enemigo_muere(sonido_muere_enemigo)


        colision_enemigo2 = pygame.sprite.spritecollide(enemigo2, grupo_disparos_jugador, True)
        if colision_enemigo2:
            enemigo2.hp -= 10
            if enemigo2.hp <= 0:
                enemigo2.enemigo_muere(sonido_muere_enemigo)


        colision_enemigo3 = pygame.sprite.spritecollide(enemigo3, grupo_disparos_jugador, True)
        if colision_enemigo3 :
            enemigo3.hp -= 10
            if enemigo3.hp <= 0:
                enemigo3.enemigo_muere(sonido_muere_enemigo)
    

        if inmunidad == False:
            # Colision de personaje - Vidas
            if pygame.sprite.spritecollide(personaje, grupo_disparos_enemigos, True):
                personaje.hp -= 1
                sonido_resta_vida.play()

            if pygame.sprite.spritecollide(personaje, grupo_enemigos, True):
                personaje.hp -= 1
                sonido_resta_vida.play()
            
            if personaje.hp <= 0 or personaje.rect.colliderect(enemigo_final.rect_coli):
                personaje.muere(sonido_muere)
                sonido_resta_vida.set_volume(0)
                FPS = 30



        if puntos > 25 and puntos <= 190:
            for enemigo in grupo_enemigos:
                enemigo.draw(pantalla)


        if puntos > 210 and puntos <= 240:
            enemigo_final.update(scroll)
            enemigo_final.draw(pantalla)
            
            colision_enemigo_final = pygame.sprite.spritecollide(enemigo_final, grupo_disparos_jugador, True)
            if colision_enemigo_final:
                enemigo_final.hp -= 20
                    

        if enemigo1.rect.left >= 200 and enemigo1.rect.left <= 202:
            enemigo_disparando = True
            for enemigo in grupo_enemigos:
                disparos_enemigos = DisparosEnemigos(enemigo.rect.x,enemigo.rect.y, 5)
                grupo_disparos_enemigos.add(disparos_enemigos)
                lista_rect_disparos.append(disparos_enemigos.rect)
        else:
            enemigo_disparando = False
        grupo_disparos_enemigos.update(scroll)
        for disparo in grupo_disparos_enemigos:
            disparo.disparo_animacion()
            disparo.draw(pantalla)
        if enemigo_disparando:
            sonido_disparo_enemigo.play()
        

        if enemigo_final.esta_disparando:
            enemigo_final_disparando = True

        if puntos >= 215:
            plataforma = Plataforma(0,ALTO_VENTANA-20,ANCHO_VENTANA,"recursos\\plataforma\\plataforma3.png")
            for plataf in grupo_plataformas:
                plataf.rect.y = ALTO_VENTANA + 50
            grupo_plataformas.add(plataforma)
            p_w = 0
            p_x = 0
            p_y = 0
            
            






        if enemigo_final_disparando and puntos > 190 and puntos <= 240 and len(grupo_enemigos) == 0 and enemigo_final.esta_muerto == False:
            enemigo1 = Enemigos(250, 50, True)
            rect_coli_enemigo1 = enemigo1.rect_coli
            enemigo2 = Enemigos(500, 160, True)
            rect_coli_enemigo2 = enemigo2.rect_coli
            enemigo3 = Enemigos(250, 270, True)
            rect_coli_enemigo3 = enemigo3.rect_coli
            lista_rect_enemigos.append(rect_coli_enemigo1)
            lista_rect_enemigos.append(rect_coli_enemigo2)
            lista_rect_enemigos.append(rect_coli_enemigo3)
            grupo_enemigos.add(enemigo1)
            grupo_enemigos.add(enemigo2)
            grupo_enemigos.add(enemigo3)
            grupo_enemigos.update(scroll)
        for enemigo in grupo_enemigos:
            enemigo.draw(pantalla)
            
        

        if puntos >= 1:
            elixir_poder.update(scroll)
            elixir_poder.draw(pantalla)
            if elixir_poder.rect.colliderect(personaje.rect):
                cantidad_disparos = 5
                sonido_recarga_poder.play()
        
        if puntos >= 20:
            elixir_vida.update(scroll)
            elixir_vida.draw(pantalla)
            if elixir_vida.rect.colliderect(personaje.rect):
                personaje.hp = 3
                sonido_recarga_vida.play()

        if cantidad_disparos == 5:
            pantalla.blit(bala,(440,770))
        if cantidad_disparos >= 4:
            pantalla.blit(bala,(470,770))
        if cantidad_disparos >= 3:
            pantalla.blit(bala,(500,770))
        if cantidad_disparos >= 2:
            pantalla.blit(bala,(530,770))
        if cantidad_disparos >= 1:
            pantalla.blit(bala,(560,770))


        if enemigo_final.esta_muerto:
            FPS = 30
            sonido_risa_enemigo.stop()
            sonido_recarga_vida.stop()
            sonido_recarga_poder.stop()
            fondo_negro = pygame.surface.Surface((ANCHO_VENTANA, ALTO_VENTANA))
            fondo_negro.fill("Black")
            draw_texto(fondo_negro, "You Win", fuente2,"Red",165,250)
            fondo_negro.set_alpha(alpha)  
            pantalla.blit(fondo_negro,(0,0))  
            inmunidad = True
            personaje.vel_y = 0
            alpha += 5
            enemigo1.kill()
            enemigo2.kill()
            enemigo3.kill()



        personaje.draw(pantalla)
        lluvia.draw_gotas(pantalla, scroll)

        

        if personaje.esta_muerto == False:
            for disparo in grupo_disparos_jugador:
                disparo.update()
                disparo.disparo_animacion()
                disparo.draw(pantalla)
                

        draw_panel(pantalla,fuente1,puntos,vida,personaje,sonido_risa_enemigo,cantidad_disparos,bala)
        
        

        if personaje.rect.top >= ALTO_VENTANA:
            sonido_muere2.play()
            fin_juego = True

        pausas = Menu(10,760, boton_de_pausa)
        if pausas.draw(pantalla, sonido_click):
            pausa = True
        
        
        if pausa:
            pantalla.blit(fondo2,(0,0)) 
            pantalla.blit(menu_de_pausa,(50,200))

            boton_reanudar = Menu(265,350,boton_de_reanudar)
            reanudar = boton_reanudar.draw(pantalla, sonido_click)

            boton_salir = Menu(350,350,boton_de_salir)
            salir = boton_salir.draw(pantalla, sonido_click)

            boton_configuracion = Menu(180,350, boton_de_conficuracion)
            if boton_configuracion.draw(pantalla, sonido_click):
                in_configuraciones = True

            if salir:
                inicio = False
                in_menu = True
                FPS = 60   
                puntos = 0
                scroll = 0
                cantidad_disparos = 0
                cronometro = 0
                personaje = Player(ANCHO_VENTANA-300,ALTO_VENTANA-150)
                grupo_plataformas.empty()
                grupo_disparos_enemigos.empty()
                grupo_disparos_jugador.empty()
                grupo_enemigos.empty()
                sonido_resta_vida.set_volume(0.5)
                lista_rect_enemigos = []
                lista_rect_disparos = []
                lista_rect_disparos_jugador = []
                elixir_poder = Poderes("recursos\\poderes\\elixir1.png")
                elixir_vida = Poderes("recursos\\poderes\\elixir_vida.png")
                plataforma = Plataforma(ANCHO_VENTANA-350,ALTO_VENTANA-50,130,"recursos\\plataforma\\plataforma3.png")
                grupo_plataformas.add(plataforma)
                enemigo_final = EnemigoFinal(ANCHO_VENTANA/2-45, 0)
                menu_configuraciones = Configuraciones(1, 0.15)
            
            if in_configuraciones:
                menu_configuraciones.draw(pantalla, fuente1, menu_de_pausa, fondo2, boton_subir_volumen, boton_bajar_volumen,sonido_click)
                    
            if reanudar:
                inmunidad = False
                pausa = False


    elif fin_juego == True:       
        if pantalla_fin_juego < ALTO_VENTANA:
            pantalla_fin_juego += 15
            fondo_negro = pygame.surface.Surface((ANCHO_VENTANA, ALTO_VENTANA))
            fondo_negro.fill("Black")
            fondo_negro.set_alpha(alpha)  
            pantalla.blit(fondo_negro,(0,0))  
            alpha += 1

        if pantalla_fin_juego > 700:
            fondo2.set_alpha(alpha)  
            pantalla.blit(fondo2,(0,0))  
            alpha += 1

        draw_texto(pantalla,"Game Over", fuente2,"Red",130,400)
        draw_texto(pantalla,"Score: "+ str(puntos), fuente1, "White",265,460)
        draw_texto(pantalla,"Precionar 'ESPACIO' para seguir", fuente1, "White",140,750)
        draw_texto(pantalla,f"Mejor score: {mejor_punto}", fuente1, "White",230,500)

        if puntos > int(mejor_punto):
            mejor_punto = puntos
            with open("score.txt", "w") as archivo:
                archivo.write(str(mejor_punto))

            
        
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            pantalla_fin_juego = 0
            fin_juego = False
            FPS = 60   
            puntos = 0
            scroll = 0
            alpha = 0
            cantidad_disparos = 0
            cronometro = 0
            personaje = Player(ANCHO_VENTANA-300,ALTO_VENTANA-150)
            grupo_plataformas.empty()
            grupo_disparos_enemigos.empty()
            grupo_disparos_jugador.empty()
            grupo_enemigos.empty()
            sonido_resta_vida.set_volume(0.5)
            lista_rect_enemigos = []
            lista_rect_disparos = []
            lista_rect_disparos_jugador = []
            elixir_poder = Poderes("recursos\\poderes\\elixir1.png")
            elixir_vida = Poderes("recursos\\poderes\\elixir_vida.png")
            plataforma = Plataforma(ANCHO_VENTANA-350,ALTO_VENTANA-50,130,"recursos\\plataforma\\plataforma3.png")
            grupo_plataformas.add(plataforma)
            enemigo_final = EnemigoFinal(ANCHO_VENTANA/2-45, 0)
            menu_configuraciones = Configuraciones(1, 0.15)
        

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()

        

        if event.type == pygame.KEYDOWN:
            if enemigo_final.esta_muerto == False:
                if event.key == pygame.K_RIGHT:
                    personaje.camina(DIRECCION_DERECHA)
                if event.key == pygame.K_LEFT:
                    personaje.camina(DIRECCION_IZQUIERDA)
                if event.key == pygame.K_UP:
                    personaje.salta()
                if event.key == pygame.K_UP and event.key == pygame.K_RIGHT:
                    personaje.salta()
                if event.key == pygame.K_UP and event.key == pygame.K_LEFT:
                    personaje.salta()
                if event.key == pygame.K_SPACE:
                    if cantidad_disparos > 0 and cantidad_disparos <= 5:
                        sonido_disparo_jugador.play()
                        personaje.ataca()
                        disparo = DisparosJugador(personaje.rect.x, personaje.rect.y,10)
                        grupo_disparos_jugador.add(disparo)
                        lista_rect_disparos_jugador.append(disparo.rect)
                        cantidad_disparos -= 1

            if event.key == pygame.K_ESCAPE:
                in_opciones = False
                in_tutorial = False
                in_configuraciones = False
                pausa = False
      

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT or event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                personaje.quieto()
                poder_activado = False

    delta_mili = tiempo.tick(FPS)
    pygame.display.flip()
    