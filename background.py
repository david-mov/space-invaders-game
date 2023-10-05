import pygame as pg
from settings import *

class Background:
    def __init__(self, game):
        self.game = game
        self.image = pg.image.load(f'{IMAGE_PATH}/background.png')
        self.y = self.image.get_height() - SCREEN_HEIGHT

    def update(self):
        if self.y <= 0:
            self.y = self.image.get_height() - SCREEN_HEIGHT
        else:
            self.y -= BACKGROUND_SPEED

    def draw(self):
        self.game.screen.blit(self.image, (0, 0), (0, self.y, SCREEN_WIDTH, SCREEN_HEIGHT))
