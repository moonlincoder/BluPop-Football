from .base import Window

'''
    Окно игры
    Тут реализуется отрисовка выбора перса, действия игроков
    В общем всё что происходит на поле
'''


class GameWindow(Window):
    def __init__(self, screen):
        super().__init__(screen)
        print("new game")
