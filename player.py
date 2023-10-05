from settings import *
import pygame as pg

class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = PLAYER_POS
        self.image = pg.image.load(f'{IMAGE_PATH}/player.png')

    def single_fire_event(self, event):
        if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
            if self.game.bullet.ready:
                self.game.sound.bullet.play()
                self.game.bullet.shot(self.x)
    
    def movement(self):
        speed = PLAYER_SPEED * self.game.delta_time
        dx = 0

        keys = pg.key.get_pressed()
        if keys[pg.K_RIGHT]:
            dx += speed
        if keys[pg.K_LEFT]:
            dx -= speed

        self.check_wall_collision(dx)

    def check_wall_collision(self, dx):
        if self.x + dx <= 0:
            self.x = 0
        elif self.x + dx >= SCREEN_WIDTH - self.image.get_width():
            self.x = SCREEN_WIDTH - self.image.get_width()
        else:
            self.x += dx

    def update(self):
        self.movement()

    def draw(self):
        self.game.screen.blit(self.image, self.pos)

    @property
    def pos(self):
        return self.x, self.y