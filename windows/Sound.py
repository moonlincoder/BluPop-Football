"""
Окно звука
"""

from windows.base import Window
from game import Game
from windows.Settings import call_menu
from core import button


class SoundWindow(Window):
    def __init__(self):
        super().__init__()
        self.btn_back = button.Button(300, 200, 50, "Назад", call_menu)

    def event_loop(self, events): ...  # События и любые действия с клавишами

    def update(self): ...  # Обновление рассчетов

    def draw(self, surface):
        surface.fill((0, 255, 255))
        self.btn_back.process(surface)
