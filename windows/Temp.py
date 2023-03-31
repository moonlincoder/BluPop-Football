import random

import pygame
from windows.base import Window

from game import Game


class TemplateWindow(Window):
    def __init__(self, i):
        self.bases = [
            [random.randint(1, pygame.display.get_window_size()[0]),
             random.randint(1, pygame.display.get_window_size()[1])] for x in range(i)
        ]

    def event_loop(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    Game.set_current_view(TemplateWindow(2))

        if pygame.key.get_pressed()[pygame.K_a]:
            self.bases[0][0] -= 10
        if pygame.key.get_pressed()[pygame.K_d]:
            self.bases[0][0] += 10
        if self.bases[0][0] > pygame.display.get_window_size()[0]:
            self.bases[0][0] = 0
        if self.bases[0][0] < 0:
            self.bases[0][0] = pygame.display.get_window_size()[0]

    def update(self):
        for a in range(len(self.bases)):
            self.bases[a][1] += 15 * (a+1)
            if self.bases[a][1] > pygame.display.get_window_size()[1]:
                self.bases[a][1] = 0

    def draw(self, surface):
        surface.fill((255, 255, 255))
        for x, y in self.bases:
            pygame.draw.circle(surface, (0, (200 if y < 300 else 0 ), 100), (x, y), 30)
