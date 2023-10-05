from settings import *
import pygame as pg

class Game_Over:
    def __init__(self, game):
        self.game = game
        self.title = self.game.large_solid_font.render('Game Over', True, TEXT_COLOR)
        self.instructions = self.game.medium_solid_font.render('Press Enter to Retry', True, TEXT_COLOR)
        self.title_pos = GAME_OVER_TITLE_POS
        self.instructions_pos = GAME_OVER_INSTRUCTIONS_POS

    def update(self):
        pass
    
    def draw(self):
        self.game.screen.blit(self.title, self.title_pos)
        self.game.screen.blit(self.instructions, self.instructions_pos)