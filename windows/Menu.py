import pygame

from core import button
from .base import Window
from game import Game

'''
    окно меню
    тут просто красивенький интерфейс и кнопка игра
    в будущем может кнопочки выбора звука
    Кнопку "о нас" не забыть
'''

def call():
    from windows import Temp
    Game.game.set_current_view(Temp.TemplateWindow(1))
class MenuWindow(Window):
    def __init__(self):
        x = pygame.display.get_width()
        y = pygame.display.get_height()
        self.but = button.Button(x, y, 200, 50, "lololo", call)
    def event_loop(self, events):
        pass

    def update(self): ...  # Обновление рассчетов

    def draw(self, surface):
        surface.fill((255, 0, 0))
        self.but.process(surface)
