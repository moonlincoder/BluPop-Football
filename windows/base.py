"""
    Базовый класс для окон
    Здесь находится общий для написания код
    Например отрисовка
    ____
    ed. Общие функции удалены, теперь это абстрактный класс
"""
from core import component


class Window:
    def __str__(self):
        return self.__class__.__name__

    def event_loop(self, events): ...  # События и любые действия с клавишами

    def update(self): ...  # Обновление рассчетов

    def draw(self, surface): ...  # Отрисовка итоговой картинки
