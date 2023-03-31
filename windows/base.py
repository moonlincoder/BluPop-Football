"""
    Базовый класс для окон
    Здесь находится общий для написания код
    Например отрисовка
"""


class Window:
    def __str__(self):
        return self.__class__.__name__

    def event_loop(self, events): ...
    def update(self): ...
    def draw(self, surface): ...
