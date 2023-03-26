from windows import MenuWindow, GameWindow
import time
import pygame
from players import base
import random


def start():
    mainClock = pygame.time.Clock()
    pygame.init()
    screen = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption("Футбол головой на двоих")

    all_sprites = pygame.sprite.Group()
    player = base.Player()
    all_sprites.add(player)

    running = True
    
    while running:
        for event in pygame.event.get():
            # проверить закрытие окна
            if event.type == pygame.QUIT:
                running = False

        screen.fill((20, 0, 0))

        button_3 = pygame.Rect(400, 420, 200, 50)
        pygame.draw.rect(screen, (153, 186, 221), button_3)

        all_sprites.update()
        all_sprites.draw(screen)

        pygame.display.update()
        mainClock.tick(60)


if __name__ == '__main__':
    start()
