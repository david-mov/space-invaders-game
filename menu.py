from settings import *
import pygame as pg

class Menu:
    def __init__(self, game):
        self.game = game
        self.title = self.game.large_solid_font.render('Space Invaders', True, TEXT_COLOR)
        self.instructions = self.game.medium_solid_font.render('Press Enter to Play', True, TEXT_COLOR)
        self.title_pos = MENU_TITLE_POS
        self.instructions_pos = MENU_INSTRUCTIONS_POS

    def update(self):
        pass

    def draw(self):
        self.game.screen.blit(self.title, self.title_pos)
        self.game.screen.blit(self.instructions, self.instructions_pos)