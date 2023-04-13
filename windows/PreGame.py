import pygame

from windows.base import Window
from windows import Temp, Football
from game import Game


class PreGameWindow(Window):
    def __init__(self):
        info_font = pygame.font.SysFont("Arial", 25)
        self.info_text1 = info_font.render("Выберите количество игроков нажав на клавиатуре [1, 2, 4]", True, (0, 10, 0))

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
                # Game.game.set_current_view(Temp.TemplateWindow(i))
                Game.game.set_current_view(Football.GameWindow([1]))
    def update(self):
        pass

    def draw(self, surface):
        surface.fill((255, 240, 240))
        text_rect = self.info_text1.get_rect()
        text_rect.center = surface.get_rect().center
        surface.blit(self.info_text1, text_rect.topleft)