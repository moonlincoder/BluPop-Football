import math

import pygame

import game
from players.player import Player
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
        self.mouse_click_start = None

    def update(self):
        self.rect.y += 10 * self.vector[0]
        self.vector[0] += 1
        self.rect.x += 10 * self.vector[1]

        if self.rect.bottom >= Game.game.screen.get_height() - 100:
            self.vector[0] -= 2
            self.vector[0] = -self.vector[0]
            self.rect.bottom = Game.game.screen.get_height() - 100

        #todo
        # if self.mouse_click_start is not None:
        #     if pygame.mouse.get_pressed()[0]:
        #

        if pygame.mouse.get_pressed()[0]:
            self.rect.center = pygame.mouse.get_pos()
            self.vector[0] = 0
        if Game.game.screen.get_width() < self.rect.right:
            self.rect.right = Game.game.screen.get_width()
            self.vector[1] = -self.vector[1]

        if self.rect.left < 0:
            self.rect.left = 0
            self.vector[1] = -self.vector[1]

        if self.rect.top < 0:
            self.rect.top = 0
            self.vector[0] = -self.vector[0]

    def collide_with_player(self, player: Player):
        if player.rect.colliderect(self.rect):
            dx = abs(player.rect.center[0] - self.rect.center[0]) - player.rect.w / 2 - self.rect.w / 2
            dy = abs(player.rect.center[1] - self.rect.center[1]) - player.rect.h / 2 - self.rect.h / 2
            if dx > dy:  # если коллизия пришлась на ось Х игрока
                self.vector[1] = -self.vector[1]
                if player.rect.x > self.rect.x:
                    self.rect.x += dx
                else:
                    self.rect.x -= dx

            else:
                self.vector[0] = -self.vector[0]
                if player.rect.y > self.rect.y:
                    self.rect.y += dy
                else:
                    self.rect.y -= dy

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class GameWindow(Window):
    def __init__(self, players: list[Player]):
        super().__init__()
        self.players = players
        self.ball = Ball(500, 500)
        print("new game")

        # debug
        # self.ball.image = pygame.Surface((100, 100))
        # for player in players:
        #     player.image = pygame.Surface((80, 160))

    def event_loop(self, events):
        for player in self.players:
            player.monitor_keys(events)

    def update(self):
        self.ball.update()
        for player in self.players:
            player.update()
            self.ball.collide_with_player(player)

    def draw(self, surface):
        surface.fill((255, 255, 255))
        self.ball.draw(surface)

        for player in self.players:
            surface.blit(player.image, player.rect)