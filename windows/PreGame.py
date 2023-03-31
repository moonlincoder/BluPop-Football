import random

import pygame

from windows.base import Window
from windows import Temp
from game import Game


class PreGameWindow(Window):
    def __init__(self):
        info_font = pygame.font.SysFont("Arial", 25)
        self.info_text1 = info_font.render("Выберите количество игроков нажав на клавиатуре [1, 2, 4]", True, (175, 175, 175))

    def event_loop(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                i = 1
                if event.key == pygame.K_1:
                    i = 1
                if event.key == pygame.K_2:
                    i = 2
                if event.key == pygame.K_4:
                    i = 4
                Game.game.set_current_view(Temp.TemplateWindow(i))

    def update(self):
        pass

    def draw(self, surface):
        surface.fill((255, 240, 240))
        overlay = pygame.Surface(surface.get_size(), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 200))
        surface.blit(overlay, (0, 0))

        text_rect = self.info_text1.get_rect()
        text_rect.center = surface.get_rect().center
        text_rect.y = surface.get_height() * 0.33

