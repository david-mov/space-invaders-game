import pygame as pg
import sys
from random import randint
from math import sqrt, pow, ceil

from settings import *
from background import *
from player import *
from bullet import *
from enemies import *
from score import *
from menu import *
from game_over import *
from sound import *

class Game:
    def __init__(self):
        pg.init()

        self.clock = pg.time.Clock()
        self.delta_time = 1

        self.screen = pg.display.set_mode(SCREEN_SIZE)
        pg.display.set_caption('Space Invaders')
        pg.display.set_icon(pg.image.load(f'{IMAGE_PATH}/icon.png'))

        pg.mixer.music.load(f'{SOUND_PATH}/background.wav')
        pg.mixer.music.play(-1)

        self.is_playing = False
        self.is_game_over = False
        self.difficulty = BASE_DIFFICULTY

        self.global_fonts()

        self.background = Background(self)
        self.sound = Sound(self)
        self.menu = Menu(self)
        self.game_over = Game_Over(self)

    def global_fonts(self):
        self.large_solid_font = pg.font.Font(f'{FONT_PATH}/font_2.ttf', 64)
        self.medium_solid_font = pg.font.Font(f'{FONT_PATH}/font_2.ttf', 32)
        self.small_solid_font = pg.font.Font(f'{FONT_PATH}/font_1.ttf', 28)

    def new_game(self):
        self.player = Player(self)
        self.enemies = Enemies(self)
        self.bullet = Bullet(self)
        self.score = Score(self)

    def check_game_over(self):
        if self.is_game_over:
            self.is_playing = False
    
    def increase_difficulty(self):
        if self.difficulty < MAX_DIFFICULTY:
            self.difficulty = self.difficulty + DIFFICULTY_INCREMENT
        else:
            self.difficulty = MAX_DIFFICULTY

    def update(self):
        self.delta_time = self.clock.tick(FPS)
        self.background.update()

        self.check_game_over()

        if not self.is_playing:
            if not self.is_game_over:
                self.menu.update()
            else:
                self.game_over.update()
                self.score.update()
        else:
            self.player.update()
            self.enemies.update()
            self.bullet.update()
        pg.display.flip()

    def draw(self):
        self.background.draw()
        if not self.is_playing:
            if not self.is_game_over:
                self.menu.draw()
            else:
                self.game_over.draw()
                self.score.draw()
        else:
            self.enemies.draw()
            self.player.draw()
            self.bullet.draw()
            self.score.draw()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN and event.key == pg.K_RETURN:
                if not self.is_playing:
                    self.is_game_over = False
                    self.is_playing = True
                    self.difficulty = 1
                    self.new_game()
            if self.is_playing:
                self.player.single_fire_event(event)

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()

if __name__ == '__main__':
    game = Game()
    game.run()