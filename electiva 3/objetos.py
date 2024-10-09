import pygame, sys, random
pygame.init()
display_info = pygame.display.Info() 
screen_size = (display_info.current_w, display_info.current_h)
screen = pygame.display.set_mode(screen_size)
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

bg = pygame.image.load("xpwallpaper.jpg")
bg = pygame.transform.scale(bg, screen_size)

bg2 = bg

bg_y = 0
bg2_y = screen_size[0]

#procesos antes de bucle principal
objetos = []
for i in range(600):
    x = random.randint(0,screen_size[1])
    y = random.randint(0, screen_size[0])
    color = random.choice(list(colores.values()))
    objetos.append([x,y,color])
    

    


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    bg_y += 1
    bg2_y += 1
    if bg_y == screen_size[0]:
        bg_y = 0

    if bg2_y == screen_size[0]:
        bg2_y = 0   

    screen.blit(bg, (bg_y, 0))
    screen.blit(bg2, (bg2_y, 0))
    
    for j in objetos:
        pygame.draw.circle(screen, j[2], j[0:2], 5)
        j[1] += 1
        j[0] += 1
        if j[1] == screen_size[1]:
            j[1] = 0

    pygame.display.update()

    pygame.display.flip()
    

    #no funciona adecuadamente la traslasion de los backgrounds