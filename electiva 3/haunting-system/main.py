import pygame
import os

pygame.init()

### SCREEN  SETTINGS ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### 
screen_size = pygame.display.Info()
screen = pygame.display.set_mode((screen_size.current_w, screen_size.current_h))
clock = pygame.time.Clock()

### ### STAGE SETTINGS ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### 
STAGE_X = 0
STAGE_Y = 0

SCALE_TILE = (int((screen_size.current_w)/10), int((screen_size.current_w)/10))
TILE_SIZE = int((screen_size.current_w)/10) 

CURRENT_PATH = os.getcwd()

grass_tile = pygame.image.load('grass.jpg')
wall_tile = pygame.image.load('wall.jpg')

scaled_grass = pygame.transform.scale(grass_tile, SCALE_TILE)
scaled_wall = pygame.transform.scale(wall_tile, SCALE_TILE)

tile_map = [
    [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 1, 1],
    [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
]

def draw_map():
    for y, row in enumerate(tile_map):
        for x, tile in enumerate(row):
            if tile == 0:
                screen.blit(scaled_grass, (x * TILE_SIZE + STAGE_X, y * TILE_SIZE + STAGE_Y))
            elif tile == 1:
                screen.blit(scaled_wall, (x * TILE_SIZE + STAGE_X, y * TILE_SIZE + STAGE_Y))


### ### COLORS ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### 

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

### ### PLAYER SETTINGS ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### 

PLAYER_X = (screen_size.current_w // 2) - 50
PLAYER_Y = (screen_size.current_h // 2) - 50
PLAYER_SPEED = 10
IS_W_PRESSED = False
IS_S_PRESSED = False
IS_A_PRESSED = False
IS_D_PRESSED = False

running = True

### ### bucle principal ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### 

while running:

    ### USER EVENTS

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_a:
                IS_A_PRESSED = True
            elif event.key == pygame.K_w:
                IS_W_PRESSED = True
            elif event.key == pygame.K_s:
                IS_S_PRESSED = True
            elif event.key == pygame.K_d:
                IS_D_PRESSED = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                IS_A_PRESSED = False
            elif event.key == pygame.K_w:
                IS_W_PRESSED = False
            elif event.key == pygame.K_s:
                IS_S_PRESSED = False
            elif event.key == pygame.K_d:
                IS_D_PRESSED = False

    ### ### logica ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ###

    ### ### player move 
    if IS_A_PRESSED:
        STAGE_X += PLAYER_SPEED
    if IS_D_PRESSED:
        STAGE_X -= PLAYER_SPEED
    if IS_S_PRESSED:
        STAGE_Y -= PLAYER_SPEED
    if IS_W_PRESSED:
        STAGE_Y += PLAYER_SPEED

    screen.fill(colores["negro" ])
    draw_map()
    print(PLAYER_X, PLAYER_Y)
    pygame.draw.rect(screen, colores["rojo"], [PLAYER_X, PLAYER_Y , 100, 100])


    

    ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ###

    clock.tick(30)
    pygame.display.flip()