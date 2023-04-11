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
    from windows import PreGame
    Game.game.set_current_view(PreGame.PreGameWindow())

def call_settings():
    from windows import Settings
    Game.game.set_current_view(Settings.SettingsWindow())
    pass

def call_sound():
    from windows import Sound
    Game.game.set_current_view(Sound.SoundWindow())
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