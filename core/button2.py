from core.component import Component
from core.label import Label
import pygame

# todo: Добавить размеры кнопки

class Button(Component):
    def __init__(self, position=(0, 0), btn_size=(0, 0), text: str = "Button", action=None, font="Arial", font_size=14):
        super().__init__()
        self.position = position

        self.btn_size = btn_size

        self.font = pygame.font.SysFont(font, font_size)
        self.text = text
        self.action = action

        # if (len(text) * font_size / 1.5 > size[0]):
        #     print(f"warn: button text may not fit. (make x-size > {len(text) * font_size // 2 + size[0] // 2})")

        self.fillColors = {
            'normal': '#ffffff',
            'hover': '#666666',
            'pressed': '#333333',
        }

        # todo:

        self.buttonRect = pygame.Rect(self.position[0], self.position[1], *self.font.size(text))
        self.buttonRect.width, self.buttonRect.height = self.btn_size

        self.buttonSurface = pygame.Surface(self.font.size(text))
        self.buttonSurf = self.font.render(text, True, (20, 20, 20))
        self.mouse_down = False

    def event_loop(self, events):
        self.buttonSurface.fill(self.fillColors['normal'])
        mousePos = pygame.mouse.get_pos()

        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors['hover'])

            if self.mouse_down:
                self.buttonSurface.fill(self.fillColors['pressed'])
                if self.action is not None and not pygame.mouse.get_pressed()[0]:
                    self.action()

        self.mouse_down = pygame.mouse.get_pressed()[0]

    def draw(self, surface):
        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width / 2 - self.buttonSurf.get_rect().width / 2,
            self.buttonRect.height / 2 - self.buttonSurf.get_rect().height / 2
        ])
        surface.blit(self.buttonSurface, self.buttonRect)
