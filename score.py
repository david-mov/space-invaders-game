from settings import *
import pygame as pg

class Score:
    def __init__(self, game):
        self.game = game
        self.points = 0

    def add_points(self, points):
        self.points += points

    def update(self):
        pass

    def draw(self):
        score = self.game.small_solid_font.render("Score : " + str(self.points), True, TEXT_COLOR)
        self.game.screen.blit(score, (SCORE_X, SCORE_Y))