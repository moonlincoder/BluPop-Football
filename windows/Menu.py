import pygame

from core import button, label, button2
from .base import Window
from game import Game


'''
    окно меню
    тут просто красивенький интерфейс и кнопка игра
    в будущем может кнопочки выбора звука
    Кнопку "о нас" не забыть
'''

window_was_resized = pygame.display.get_surface().get_rect()

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
        super().__init__()

        self.add_child(label.Label((50, 50), "Футбик головой", font_size=42))
        self.add_child(label.Label((50, 170), "в новой кнопке нажатие срабатывает при отпускании", font_size=25,
                                   color=(150, 250, 100)))
        self.add_child(button2.Button((430, 100), (500, 40), "Получить 3 точки", font_size=50, action=call))

        self.add_child(button2.Button((430, 400), (350, 40), "Игра", font_size=50, action=call))
        self.add_child(button2.Button((430, 500), (350, 40), "Настройки", font_size=50, action=call_settings))
        self.add_child(button2.Button((430, 600), (350, 40), "Звук", font_size=50, action=call_sound))

    def event_loop(self, event):
        pass

    def update(self):
        # todo: Отслеживание изменения размеров окна, чтобы можно было увеличить кнопки
        if pygame.display.get_surface().get_rect() > window_was_resized:
            resized_x = pygame.display.get_surface().get_rect().w - window_was_resized.w
            resized_y = pygame.display.get_surface().get_rect().h - window_was_resized.h

            self.percent_x = (100 * pygame.display.get_surface().get_rect().w / window_was_resized.w) - 100
            self.percent_y = (100 * pygame.display.get_surface().get_rect().h / window_was_resized.h) - 100

            print(f"Window was resized ({resized_x}: {self.percent_x}%, {resized_y}: {self.percent_y}%)")


    def draw(self, surface):
        surface.fill((255, 0, 0))

        #button2.size *= self.percent_x