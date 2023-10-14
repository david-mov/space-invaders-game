import pygame as pg
from settings import *

class Bullet:
    def __init__(self, game):
        self.game = game
        self.image = pg.image.load(f'{IMAGE_PATH}/bullet.png')
        self.speed = BULLET_SPEED * self.game.delta_time
        self.ready = True
        self.x = self.game.player.x + BULLET_X_DIST
        self.y = self.game.player.y + BULLET_Y_DIST

    def reset(self):
        self.ready = True
        self.y = self.game.player.y + BULLET_Y_DIST

    def shot(self, player_x):
        self.x = player_x + BULLET_X_DIST
        self.ready = False

    def update(self):
        if not self.ready:
            self.y -= self.speed
            if self.y <= -self.image.get_height():
                self.reset()

    def draw(self):
        if not self.ready:
            self.game.screen.blit(self.image, (self.x, self.y))