import pygame

from windows.base import Window
from windows import Temp, Football
from game import Game

from players.base import CONTROL_1, CONTROL_2, CONTROL_3, CONTROL_4
from players import Bean


class PreGameWindow(Window):
    def __init__(self):
        super().__init__()
        info_font = pygame.font.SysFont("Arial", 25)
        self.info_text1 = info_font.render("Выберите количество игроков нажав на клавиатуре [1, 2, 4]", True, (0, 10, 0))

    def event_loop(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                selected = []
                if event.key == pygame.K_1:
                    selected.append(Bean(100, 100, CONTROL_2))
                if event.key == pygame.K_2:
                    selected.append(Bean(400, 100, CONTROL_1))
                    selected.append(Bean(100, 100, CONTROL_2))
                if event.key == pygame.K_4:
                    selected.append(Bean(100, 100, CONTROL_1))
                    selected.append(Bean(300, 100, CONTROL_2))
                    selected.append(Bean(500, 100, CONTROL_3))
                    selected.append(Bean(700, 100, CONTROL_4))

                Game.game.set_current_view(Football.GameWindow(selected))

    def update(self):
        pass

    def draw(self, surface):
        surface.fill((255, 240, 240))
        text_rect = self.info_text1.get_rect()
        text_rect.center = surface.get_rect().center
        surface.blit(self.info_text1, text_rect.topleft)