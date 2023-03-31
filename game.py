import pygame
from windows import Window


class Game:
    game: 'Game' = None

    def __init__(self):
        Game.game = self

        pygame.init()
        pygame.font.init()

        WIDTH = 1280
        HEIGHT = 960
        GAME_TITLE = "Футбол головой на двоих"

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(GAME_TITLE)
        self.clock = pygame.time.Clock()
        self.current_view: Window = Window()

    @staticmethod
    def set_current_view(view):
        Game.game.current_view = view

    def run(self):
        from windows import Temp
        self.current_view = Temp.TemplateWindow()
        running = True
        while running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                elif event.type == pygame.QUIT:
                    running = False

            self.current_view.event_loop(events)
            self.current_view.update()
            self.current_view.draw(self.screen)

            # Эти две строки должны быть в самом конце цикла
            pygame.display.flip()
            self.clock.tick(30)
            # ---------------------------

        pygame.quit()
