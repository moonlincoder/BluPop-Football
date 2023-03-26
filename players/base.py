import pygame

'''
    Базовый класс для персонажей
    Здесь находится общий для написания код
    Например отрисовка спрайтов
'''


class Player(pygame.sprite.Sprite):
    sprite = ''

    def __init__(self):
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
        pass

    # def draw(self, surface):
    #     # img = pygame.transform.flip(self.image, self.flip, False)
    #     # surface.blit(img, (self.rect.x - (self.offset[0] * self.image_scale), self.rect.y - (
    #     #     self.offset[1] * self.image_scale)))
    #     surface.draw(rect)
