import pygame
import os

pygame.init()

### SCREEN  SETTINGS ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### 
screen_size = pygame.display.Info()
screen = pygame.display.set_mode((screen_size.current_w, screen_size.current_h))
clock = pygame.time.Clock()

### ### PLAYER SETTINGS ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### 
PLAYER = {
    "w" : 100,
    "h" : 100,
    "x" : (screen_size.current_w // 2) - 50,
    "y" : (screen_size.current_h // 2) - 50, 
    "speed" : 10,

}
IS_W_PRESSED = False
IS_S_PRESSED = False
IS_A_PRESSED = False
IS_D_PRESSED = False

running = True



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

def colision (obj1, obj2):
    return obj1['x'] < obj2['x']+obj2['w'] and obj1['x'] + obj1['w'] > obj2['y']  and  obj1['y'] < obj2['y']+obj2['h'] and obj1['y'] + obj1['h'] > obj2['y']

def side_colision(obj1, obj2):    
    dist_left = obj2['x'] - (obj1['x'] + obj1['w'])
    dist_right = (obj2['x'] + obj2['w']) - obj1['x']
    dist_top = obj2['y'] - (obj1['y'] + obj1['h'])
    dist_bottom = (obj2['y'] + obj2['h']) - obj1['y']

    min_distance = min(dist_left, dist_right, dist_top, dist_bottom)
    if min_distance == dist_left:
        return "LEFT"
    elif min_distance == dist_right:
        return "RIGHT"
    elif min_distance == dist_top:
        return "UP"
    elif min_distance == dist_bottom:
        return "DOWN"

    return False

        

def draw_map():
    global IS_A_PRESSED, IS_D_PRESSED, IS_S_PRESSED, IS_W_PRESSED
    for y, row in enumerate(tile_map):
        for x, tile in enumerate(row):
            if tile == 0:
                screen.blit(scaled_grass, (x * TILE_SIZE + STAGE_X, y * TILE_SIZE + STAGE_Y))
            elif tile == 1: ### wall
                screen.blit(scaled_wall, (x * TILE_SIZE + STAGE_X, y * TILE_SIZE + STAGE_Y))
                OBJECT = {
                    'x' : x * TILE_SIZE + STAGE_X,
                    'y' : y * TILE_SIZE + STAGE_Y,
                    'w' : TILE_SIZE,
                    'h' : TILE_SIZE
                }
                if(colision(PLAYER, OBJECT)):
                    COLISION = side_colision(PLAYER, OBJECT)
                    if COLISION == "UP":
                        IS_W_PRESSED = False
                        print("up")
                    if COLISION == "DOWN":
                        IS_S_PRESSED = False
                        print("down")
                    if COLISION == "LEFT":
                        IS_A_PRESSED = False
                        print("left")
                    if COLISION == "RIGHT":
                        IS_D_PRESSED = False
                        print("right")


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

    

    ### ### screen drawing

    screen.fill(colores["negro" ])
    draw_map()
    pygame.draw.rect(screen, colores["rojo"], [PLAYER["x"], PLAYER['y'] , PLAYER['w'], PLAYER['h']])

    ### ### player movement
    if IS_A_PRESSED:
        STAGE_X += PLAYER['speed']
    if IS_D_PRESSED:
        STAGE_X -= PLAYER['speed']
    if IS_S_PRESSED:
        STAGE_Y -= PLAYER['speed']
    if IS_W_PRESSED:
        STAGE_Y += PLAYER['speed']


    

    ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ###

    clock.tick(30)
    pygame.display.flip()