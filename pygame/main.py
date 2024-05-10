import pygame, sys, random
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

#procesos antes de bucle principal
objetos = []
for i in range(600):
    x = random.randint(0,screen_size.current_w)
    y = random.randint(0, screen_size.current_h)
    color = random.choice(list(colores.values()))
    objetos.append([x,y,color])
    

    

#bucle principal

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    #logica
    screen.fill(colores["negro"])
    for j in objetos:
        pygame.draw.circle(screen, j[2], j[0:2], 5)
        j[1] += 1
        j[0] += 1
        if j[1] == screen_size.current_h:
            j[1] = 0
    clock.tick(30)
    pygame.display.flip()