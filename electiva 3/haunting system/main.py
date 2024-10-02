import pygame, sys, random
import escenario

pygame.init()
screen_size = pygame.display.Info()
screen = pygame.display.set_mode((screen_size.current_w, screen_size.current_h))
clock = pygame.time.Clock()

colores = {
    "rojo": (255, 0, 0),
    "verde": (0, 255, 0),
    "azul": (0, 0, 255),
    "amarillo": (255, 255, 0),
    "negro": (0, 0, 0),
    "blanco": (255, 255, 255),
    "gris": (128, 128, 128),
    "rosa": (255, 192, 203),
    "naranja": (255, 165, 0),
    "morado": (128, 0, 128),
    "turquesa": (0, 255, 255),
    "celeste": (175, 238, 238),
    "marrón": (165, 42, 42),
    "dorado": (218, 165, 32),
    "plateado": (192, 192, 192),
}

cube_x = 0
cube_y = 0
running = True

map_size = (4000,4000)

#bucle principal
escenario.simple()
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_a:
                cube_y -= 5
            elif event.key == pygame.K_w:
                cube_x -= 5
            elif event.key == pygame.K_s:
                cube_x += 5
            elif event.key == pygame.K_d:
                cube_y += 5

    ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ###

    #logica
    screen.fill(colores["negro" ])
    pygame.draw.rect(screen, colores["rojo"], [cube_x, cube_y, 100, 100])


    

    ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ###

    clock.tick(30)
    pygame.display.flip()