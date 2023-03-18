from .windows import MenuWindow, GameWindow
import time
import pygame


def start():
    menu = MenuWindow()

    draw = menu

    while True:

        try:
            draw.show()
            time.sleep(0.5)
        except:
            newgame = GameWindow()
            draw = newgame



if __name__ == '__main__':
    start()