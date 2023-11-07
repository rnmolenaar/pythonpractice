import pygame
pygame.init()

screen_width = 1200
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))

player = pygame.Rect((100, 400, 60, 60))

run = True
while run:

    screen.fill((240, 240, 240))

    pygame.draw.rect(screen, (50, 0, 50), player)

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]  == True:
        player.move_ip(-1, 0)
    elif key[pygame.K_RIGHT]  == True:
        player.move_ip(1, 0)
    elif key[pygame.K_UP]  == True:
        player.move_ip(0, -1)
    elif key[pygame.K_DOWN]  == True:
        player.move_ip(0, 1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
