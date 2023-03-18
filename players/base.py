'''
    Базовый класс для персонажей
    Здесь находится общий для написания код
    Например отрисовка спрайтов
'''


class Player:
    sprite = ''

    def __init__(self):
        self.rect = pygame.Rect((x, y, 80, 180))

        self.action = 0
        # 0: idle
        # 1: run
        # 2: jump
        # 3: attack1
        # 4: attack2


    def monitor_keys():
        pass

    def draw(self, surface):
        # img = pygame.transform.flip(self.image, self.flip, False)
        # surface.blit(img, (self.rect.x - (self.offset[0] * self.image_scale), self.rect.y - (
        #     self.offset[1] * self.image_scale)))
        surface.draw(rect)