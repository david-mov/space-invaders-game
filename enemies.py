from settings import *
import pygame as pg
from random import randint
from enemy import *

class Enemies:
    def __init__(self, game):
        self.game = game
        self.num_of_enemies = NUM_OF_ENEMIES
        self.enemies = []
        self.images = [pg.image.load(enemy) for enemy in ENEMY_IMAGES]
        self.generate_many()
    
    def generate_one_random(self):
        variation = randint(0, NUM_OF_ENEMY_CATEGORIES-1)
        self.enemies.append(Enemy(self.game, variation, self.images[variation]))
    
    def generate_many(self):
        for n in range(1, self.num_of_enemies):
            self.generate_one_random()

    def check_dead(self, idx):
        if not self.enemies[idx].alive:
            self.enemies.pop(idx)
            self.generate_one_random()

    def update(self):
        for idx in range(len(self.enemies)):
            self.enemies[idx].update()
            self.check_dead(idx)

    def draw(self):
        [enemy.draw() for enemy in self.enemies]