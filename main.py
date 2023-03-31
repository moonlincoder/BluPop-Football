import pygame
from windows import *
from players import base

WIDTH, HEIGHT = 1171, 700
GAME_TITLE = "Футбол головой на двоих"

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# all_sprites = pygame.sprite.Group()
# player = base.Player()
# all_sprites.add(player)

running = True
display = Menu.MenuWindow(screen)

while running:
    for event in pygame.event.get():
        # проверить закрытие окна
        if event.type == pygame.QUIT:
            running = False

    display.update()
    pygame.time.wait(1000)
    clock.tick(60)
    pygame.display.update()
    screen.fill((20, 0, 0))

    # button_3 = pygame.Rect(400, 420, 200, 50)
    # pygame.draw.rect(screen, (153, 186, 221), button_3)
    #
    # all_sprites.update()
    # all_sprites.draw(screen)



