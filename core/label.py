from core.component import Component
import pygame


class Label(Component):
    def __init__(self, position=(0, 0), label_size=(0, 0), text: str = "Пома", font="monospace", font_size=14, color=(255, 255, 255)):
        super().__init__()
        self.position = position
        self.text = text
        self.font = font
        # self.font_size = font_size
        # self.color = color
        self.label = pygame.font.SysFont(font, font_size).render(f'{text}', True, color)

        self.label_size = label_size

        self.labelRect = pygame.Rect(self.position, self.label_size)
        self.labelRect.width, self.labelRect.height = self.label_size

    def draw(self, surface):
        if self.label is not None:
            surface.blit(self.label, self.position)
