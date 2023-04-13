"""
Окно настроек
Выбор на полноэкранный \ оконный

"""


from windows.base import Window
from game import Game
from core import button


def call_menu():
    from windows import Menu
    Game.game.set_current_view(Menu.MenuWindow())


class SettingsWindow(Window):
    def __init__(self):
        self.btn_back = button.Button(300, 200, 50, "Назад", call_menu)

    def event_loop(self, events): ...  # События и любые действия с клавишами
    def update(self): ...  # Обновление рассчетов
    def draw(self, surface):
        surface.fill((255, 255, 0))

        self.btn_back.process(surface)
