import pygame

from game import Game
from .base import Window

'''
    Окно игры
    Тут реализуется отрисовка выбора перса, действия игроков
    В общем всё что происходит на поле
'''


class Ball(pygame.sprite.Sprite):
    def __init__(self, x=100, y=100):
        super().__init__()
        self.vector = [2, 1]

        self.image = pygame.image.load("./assets/images/ball.png")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.y += 10 * self.vector[0]
        self.vector[0] += 1
        self.rect.x += 10 * self.vector[1]

        if self.rect.bottom >= Game.game.screen.get_height():
            self.vector[0] -= 2
            self.vector[0] = -self.vector[0]
            self.rect.bottom = Game.game.screen.get_height()

        if pygame.mouse.get_pressed()[0]:
            self.rect.center = pygame.mouse.get_pos()

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class GameWindow(Window):
    def __init__(self, players):
        self.players = players
        self.ball = Ball()
        print("new game")

    def update(self):
        self.ball.update()

    def draw(self, surface):
        surface.fill((255, 255, 255))
        self.ball.draw(surface)
