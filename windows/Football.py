import pygame

from core import label
from players.player import Player
from game import Game
from windows.Menu import MenuWindow
from windows.base import Window

'''
    Окно игры
    Тут реализуется отрисовка выбора перса, действия игроков
    В общем всё что происходит на поле
'''


class Ball(pygame.sprite.Sprite):
    def __init__(self, x=100, y=100):
        super().__init__()
        self.vector = [2, 1]

        self.image = pygame.image.load("./assets/images/ball.png")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
        self.mouse_click_start = None

    def update(self):
        self.rect.y += 10 * self.vector[0]
        self.vector[0] += 1
        self.rect.x += 10 * self.vector[1]

        if self.rect.bottom >= Game.game.screen.get_height() - 100:
            self.vector[0] -= 2
            self.vector[0] = -self.vector[0]
            self.rect.bottom = Game.game.screen.get_height() - 100

        #todo
        # if self.mouse_click_start is not None:
        #     if pygame.mouse.get_pressed()[0]:
        #

        if pygame.mouse.get_pressed()[0]:
            self.rect.center = pygame.mouse.get_pos()
            self.vector[0] = 0
        if Game.game.screen.get_width() < self.rect.right:
            self.rect.right = Game.game.screen.get_width()
            self.vector[1] = -self.vector[1]

        if self.rect.left < 0:
            self.rect.left = 0
            self.vector[1] = -self.vector[1]

        if self.rect.top < 0:
            self.rect.top = 0
            self.vector[0] = -self.vector[0]

        self.vector[0] *= 0.95
        self.vector[1] *= 0.95

    def collide_with_player(self, player: Player):
        if player.rect.colliderect(self.rect):
            dx = abs(player.rect.center[0] - self.rect.center[0]) - player.rect.w / 2 - self.rect.w / 2
            dy = abs(player.rect.center[1] - self.rect.center[1]) - player.rect.h / 2 - self.rect.h / 2
            if dx > dy:  # если коллизия пришлась на ось Х игрока
                self.vector[1] = -self.vector[1]
                if player.rect.x > self.rect.x:
                    self.rect.x += dx
                else:
                    self.rect.x -= dx

            else:
                self.vector[0] = -self.vector[0]
                if player.rect.y > self.rect.y:
                    self.rect.y += dy
                else:
                    self.rect.y -= dy

    def collide_with_gate(self, gate) -> bool:
        '''
        if self.rect.bottom <= gate.rect.top:
            if abs(self.rect.center[0] - gate.rect.center[0]) < 20:
                    return True

        elif self.rect.bottom == gate.rect.top:
            self.vector[1] = -self.vector[1]

        return False
        '''

        # if self.rect.
        #     self.vector[0] = -self.vector[0]
        #     self.rect.bottom = gate.rect.top - 10




    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Gate(pygame.sprite.Sprite):
    def __init__(self, x, y, image_loc):
        super().__init__()

        self.image = pygame.image.load(image_loc)
        self.image = pygame.transform.scale(self.image, (150, 300))
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y


    def draw(self, surface):
        surface.blit(self.image, self.rect)
        #surface.fill((255, 255, 255))



class GameWindow(Window):
    def __init__(self, players: list[Player]):
        self.scoreLeft, self.scoreRight = 0, 0
        super().__init__()
        self.players = players
        self.ball = Ball(500, 500)
        self.GateLeft = Gate(0, Game.game.screen.get_height() - 400, "./assets/images/Goals/goalLeft.png")
        self.GateRight = Gate(Game.game.screen.get_width() - 150, Game.game.screen.get_height() - 400, "./assets/images/Goals/goalRight.png")

        self.bg = pygame.image.load('./assets/images/background.png')

        print("new game")

        self.label = label.Label((Game.game.screen.get_width() / 2 - 50, 50), "0 | 0", font_size=50)

        # debug
        # self.ball.image = pygame.Surface((100, 100))
        # self.ball.image.fill((200,200,40))
        # self.GateLeft.image = pygame.Surface((150, 300))
        # self.GateRight.image = pygame.Surface((150, 300))
        # for player in players:
        #     player.image = pygame.Surface((80, 160))

    def event_loop(self, events):
        for player in self.players:
            player.monitor_keys(events, self)

    def update(self):
        self.ball.update()
        for player in self.players:
            player.update()
            self.ball.collide_with_player(player)

        if abs(self.ball.rect.bottom - (Game.game.screen.get_height() - 400)) < 25 and (self.ball.rect.center[0] < 150 or self.ball.rect.center[0] > (Game.game.screen.get_width() - 150)):
            self.ball.vector[0] = -self.ball.vector[0]
        elif self.ball.rect.bottom >= Game.game.screen.get_height() - 400:
            if self.ball.rect.center[0] < 150:
                self.scoreRight += 1
                self.new_game([-1, -1])

            if self.ball.rect.center[0] > (Game.game.screen.get_width() - 150):
                self.scoreLeft += 1
                self.new_game([-1, 1])

        if pygame.key.get_pressed()[pygame.K_BACKQUOTE]:
            self.scoreLeft += 1
            self.scoreRight += 1
            self.new_game()

        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            Game.game.set_current_view(MenuWindow())

    def new_game(self, vel=[-1, -2]):
        self.ball.rect.center = Game.game.screen.get_rect().center
        self.ball.vector = vel
        self.label.text = f'{self.scoreLeft} | {self.scoreRight}'


    def draw(self, surface):
        #surface.fill((255, 255, 255))
        self.bg = pygame.transform.scale(self.bg, (Game.game.screen.get_size()))
        surface.blit(self.bg, (0, 0))

        self.ball.draw(surface)

        for player in self.players:
            surface.blit(player.image, player.rect)

        self.GateLeft.draw(surface)
        self.GateRight.draw(surface)
        self.label.draw(surface)
