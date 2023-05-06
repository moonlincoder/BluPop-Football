from core.component import Component
import pygame


class Label(Component):
    def __init__(self, position=(0, 0), text: str = "Пома", font="monospace", font_size=14, color=(255, 255, 255)):
        super().__init__()
        self.position = position
        self.text = text
        self.font = font
        self.font_size = font_size
        self.color = color

    def draw(self, surface):
        if self.text is not None:
            label = pygame.font.SysFont(self.font, self.font_size).render(f'{self.text}', True, self.color)
            surface.blit(label, self.position)
