import pygame as pg
from settings import *

class Sound:
    def __init__(self, game):
        self.game = game
        pg.mixer.init()
        self.path = SOUND_PATH

        self.bullet = pg.mixer.Sound(f'{SOUND_PATH}/laser.wav')
        self.explosion = pg.mixer.Sound(f'{SOUND_PATH}/explosion.wav')
        self.game_over = pg.mixer.Sound(f'{SOUND_PATH}/game_over.wav')