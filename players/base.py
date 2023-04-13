import pygame

'''
    Базовый класс для персонажей
    Здесь находится общий для написания код
    Например отрисовка спрайтов
'''

CONTROL_1 = ('up', 'left', 'down', 'right', pygame.K_SLASH)
CONTROL_2 = ('w', 'a', 's', 'd', pygame.K_TAB)
CONTROL_3 = ('u', 'h', 'j', 'k', pygame.K_SPACE)
CONTROL_4 = ('8', '4', '2', '6', '0')


class Player(pygame.sprite.Sprite):
    sprite = ''

    def __init__(self, x_pos, y_pos, controls):

        self.x_pos = x_pos
        self.y_pos = y_pos

        self.score = 0

        self.controls = controls
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 200, 0))

        self.rect = self.image.get_rect()
        self.rect.center = [100, 100]

        self.action = 0
        # 0: idle
        # 1: run
        # 2: jump
        # 3: attack1
        # 4: attack2

    def update(self):
        self.rect.x += 5
        if self.rect.left > 1000:
            self.rect.x = 0


    def monitor_keys(self):
        self.move_value = 0
        self.rotate_value = 0


