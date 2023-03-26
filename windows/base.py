'''
    Базовый класс для окон
    Здесь находится общий для написания код
    Например отрисовка
'''


class Window:
    def show(self):
        print(f"drawing {str(self)}")

    def __str__(self):
        return self.__class__.__name__
