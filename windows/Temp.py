import random

import pygame

from windows.base import Window
from game import Game

class TemplateWindow(Window):
    def __init__(self):
        self.x = random.randint(1, pygame.display.get_window_size()[0])
        self.y = random.randint(1, pygame.display.get_window_size()[1])

    def event_loop(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    Game.set_current_view(TemplateWindow())

        if pygame.key.get_pressed()[pygame.K_a]:
            self.x -= 5
        if pygame.key.get_pressed()[pygame.K_d]:
            self.x += 5
        if self.x > pygame.display.get_window_size()[0]:
            self.x = 0
        if self.x < 0:
            self.x = pygame.display.get_window_size()[0]


    def update(self):
        self.y += 20
        if self.y > pygame.display.get_window_size()[1]:
            self.y = 0

    def draw(self, surface):
        surface.fill((255, 255, 255))
        pygame.draw.circle(surface, (0, 0, 200), (self.x, self.y), 30)