import pygame as pg
from settings import *
from math import sqrt, pow, ceil
from random import randint

class Enemy:
    def __init__(self, game, variation, image):
        self.game = game
        self.image = image
        self.alive = True
        self.x_speed = (variation + 1) * self.game.difficulty
        self.y_speed = (variation + 1) * self.game.difficulty
        self.x = randint(0, SCREEN_WIDTH - self.image.get_width())
        self.y = - self.image.get_height()
        self.points = ceil((variation + 1) * self.game.difficulty)

    def movement(self):
        if self.x <= 0 or self.x >= SCREEN_WIDTH - self.image.get_width():
             self.x_speed = -self.x_speed
             self.y += self.y_speed
        else:
             self.x += self.x_speed

    def check_invasion(self):
        if self.y >= SCREEN_HEIGHT:
            self.game.is_game_over = True
        
    def check_shot(self):
        bullet_enemy_dist = sqrt(pow(self.x - self.game.bullet.x, 2) + (pow(self.y - self.game.bullet.y, 2)))
        if bullet_enemy_dist < COLLISION_SCOPE and not self.game.bullet.ready:
            self.game.sound.explosion.play()
            self.alive = False
            self.game.bullet.reset()
            self.game.score.add_points(self.points)
            self.game.increase_difficulty()

    def update(self):
        self.movement()
        self.check_shot()
        self.check_invasion()

    def draw(self):
        self.game.screen.blit(self.image, self.pos)

    @property
    def pos(self):
        return self.x, self.y