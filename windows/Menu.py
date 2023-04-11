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

def call_settings():
    # вызов окна с настройками
    pass

def call_sound():
    # окно со звуком
    pass


class MenuWindow(Window):
    def __init__(self):
        self.btn_game = button.Button(0, 200, 50, "Игра", call)

        # отступ
        self.btn_settings = button.Button(70, 200, 50, "Настройки", call_settings)
        # еше одна кнопочка с отступом, скорее всего стоит реализовать по-другому
        self.btn_sound = button.Button(140, 200, 50, "Звук", call_sound)

    def event_loop(self, events):
        pass

    def update(self): ...  # Обновление рассчетов

    def draw(self, surface):
        surface.fill((255, 0, 0))

        self.btn_game.process(surface)
        self.btn_settings.process(surface)
        self.btn_sound.process(surface)