from .base import Window

'''
    Окно игры
    Тут реализуется отрисовка выбора перса, действия игроков
    В общем всё что происходит на поле
'''


class GameWindow(Window):
    wind_created = 0

    def __init__(self):
        self.wind_created += 1
        print("new game")

    def __str__(self):
        return self.__class__.__name__ + str(self.wind_created)

    def choosing_pers(self):
        pass

    def game(self):
        pass