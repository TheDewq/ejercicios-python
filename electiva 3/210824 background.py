import pygame, sys
pygame.init()
display_info = pygame.display.Info() 
screen_size = (display_info.current_w, display_info.current_h)
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()

bg = pygame.image.load("electiva 3/xpwallpaper.jpg")
bg = pygame.transform.scale(bg, screen_size)

bg2 = bg

bg_y = 0
bg2_y = screen_size[0]


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

    pygame.display.update()

    pygame.display.flip()
    

    #no funciona adecuadamente la traslasion de los backgrounds