import pygame

from core.component import Component


class Button(Component):
    def __init__(self, indent, width, height, buttonText='Button', onclickFunction=None):
        self.indent = indent

        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction

        self.fillColors = {
            'normal': '#ffffff',
            'hover': '#666666',
            'pressed': '#333333',
        }

        font = pygame.font.SysFont('Arial', 40)
        self.buttonSurface = pygame.Surface((self.width, self.height))

        self.buttonSurf = font.render(buttonText, True, (20, 20, 20))

        self.alreadyPressed = False

    def process(self, screen, x=-1, y=-1):

        # ширина и высота экрана
        if x < 0 and y < 0:
            self.x = pygame.display.get_surface().get_width() / 2 - self.width / 2
            self.y = pygame.display.get_surface().get_height() / 2 + self.indent - self.height / 2

        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        mousePos = pygame.mouse.get_pos()

        self.buttonSurface.fill(self.fillColors['normal'])
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors['hover'])

            if pygame.mouse.get_pressed()[0]:
                self.buttonSurface.fill(self.fillColors['pressed'])

                if self.onclickFunction is not None:
                    self.onclickFunction()

        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width / 2 - self.buttonSurf.get_rect().width / 2,
            self.buttonRect.height / 2 - self.buttonSurf.get_rect().height / 2
        ])

        screen.blit(self.buttonSurface, self.buttonRect)
