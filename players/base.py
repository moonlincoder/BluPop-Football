import pygame
import gif_pygame
from game import Game

'''
    Базовый класс для персонажей
    Здесь находится общий для написания код
    Например отрисовка спрайтов
'''


class Controls:
    def __init__(self, up, down, left, right, extra):
        self.up = up
        self.down = down
        self.left = left
        self.right = right
        self.extra = extra


CONTROL_1 = Controls(pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_SLASH)
CONTROL_2 = Controls(pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d, pygame.K_TAB)
CONTROL_3 = Controls(pygame.K_u, pygame.K_j, pygame.K_h, pygame.K_k, pygame.K_SPACE)
CONTROL_4 = Controls(pygame.K_8, pygame.K_5, pygame.K_4, pygame.K_6, pygame.K_0)


class Player(pygame.sprite.Sprite):
    sprite = './assets/images/bean/idle.png'
    run = ''
    jump = './assets/images/bean/jump.gif'
    kick = ''

    def __init__(self, x_pos, y_pos, controls):
        self.score = 0

        # self.move_value = 0
        # self.rotate_value = 0

        self.controls = controls
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(self.sprite)
        self.image = pygame.transform.scale(self.image, (80, 160))

        self.rect = self.image.get_rect()
        self.rect.center = [x_pos, y_pos]

        self.action = 0
        # 0: idle
        # 1: run
        # 2: jump
        # 3: attack1
        # 4: attack2

    def update(self):
        if self.rect.left > 1000:
            self.rect.x = 0

        if self.rect.bottom < Game.game.screen.get_height() - 100:
            self.rect.y += 20
        else:
            self.rect.bottom = Game.game.screen.get_height() - 100

    def monitor_keys(self, events):
        if pygame.key.get_pressed()[self.controls.up]:
            self.rect.y -= 100

        if pygame.key.get_pressed()[self.controls.down]:
            pass    # связать игрока с мячом
                    # копать в сторону object collision

        if pygame.key.get_pressed()[self.controls.left]:
            self.rect.x -= 5
        if pygame.key.get_pressed()[self.controls.right]:
            self.rect.x += 5