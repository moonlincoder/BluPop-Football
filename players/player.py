import pygame
from game import Game

'''
    Базовый класс для персонажей
    Здесь находится общий для написания код
    Например отрисовка спрайтов
'''


# todo: Добавить границы игрового поля

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

        self.speed = [0, 0]

        self.controls = controls
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(self.sprite)
        self.image = pygame.transform.scale(self.image, (80, 160))

        self.rect = self.image.get_rect()
        self.rect.center = [x_pos, y_pos]

        self.jumping = False
        self.jump_pressed = False
        self.double_jumping = False
        self.running = False
        self.kicking = False

    def update(self):
        if self.rect.right >= Game.game.screen.get_width():
            self.rect.right = Game.game.screen.get_width()
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.top <= 0:
            self.rect.top = 0

        if self.rect.bottom < Game.game.screen.get_height() - 100:
            self.rect.y += 20  # todo: перейти на перемещение от скорости вместо перетаскивания игрока
        else:
            self.rect.bottom = Game.game.screen.get_height() - 100
            self.jumping = False
            self.double_jumping = False

    def monitor_keys(self, events):
        if pygame.key.get_pressed()[self.controls.up]:
            if self.jumping:
                if not self.double_jumping and not self.jump_pressed:
                    self.double_jumping = True
                    self.rect.y -= 150
            else:
                self.jumping = True
                self.rect.y -= 250
            self.jump_pressed = True
        else:
            self.jump_pressed = False


        if pygame.key.get_pressed()[self.controls.down]:
            pass
            # todo: связать игрока с мячом
            # todo: копать в сторону object collision

        if pygame.key.get_pressed()[self.controls.left]:
            self.rect.x -= 20
        if pygame.key.get_pressed()[self.controls.right]:
            self.rect.x += 20
