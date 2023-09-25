import pygame
import sys
from os.path import abspath, dirname
from random import randint
from math import sqrt, pow, ceil

BASE_PATH = abspath(dirname(__file__))

FONT_PATH = BASE_PATH + '/fonts'
IMAGE_PATH = BASE_PATH + '/images'
SOUND_PATH = BASE_PATH + '/sounds'

GOLDEN_COLOR = (245, 191, 3)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

pygame.init()

# Screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Space Invaders')

icon = pygame.image.load(f'{IMAGE_PATH}/icon.png')
pygame.display.set_icon(icon)

FPS = 60
clock = pygame.time.Clock()

# Background
background_img = pygame.image.load(f'{IMAGE_PATH}/background.png')
background_y = background_img.get_height() - SCREEN_HEIGHT

# Music
pygame.mixer.music.load(f'{SOUND_PATH}/background.wav')
pygame.mixer.music.play(-1)

# Fonts
title_font = pygame.font.Font(f'{FONT_PATH}/font_2.ttf', 64)
subtitle_font = pygame.font.Font(f'{FONT_PATH}/font_2.ttf', 32)
score_font = pygame.font.Font(f'{FONT_PATH}/font_1.ttf', 28)

def render_background():
    global background_y
    if background_y <= 0:
        background_y = background_img.get_height() - SCREEN_HEIGHT
    else:
        background_y -= 2.5
    screen.blit(background_img, (0, 0), (0, background_y, SCREEN_WIDTH, SCREEN_HEIGHT))

# Player
playing = False

player_img = pygame.image.load(f'{IMAGE_PATH}/player.png')
player_x = 370
player_y = 450
player_x_change = 0

def render_player(x, y):
    screen.blit(player_img, (x, y))

# Enemy
num_of_enemies = 3
difficulty = 1

ENEMY_IMAGES = ['enemy_1', 'enemy_2', 'enemy_3', 'enemy_4']
for idx in range(len(ENEMY_IMAGES)):
    ENEMY_IMAGES[idx] = pygame.image.load(f'{IMAGE_PATH}/{ENEMY_IMAGES[idx]}.png')

ENEMY_CATEGORIES_COUNT = len(ENEMY_IMAGES)

enemies = []

def create_enemy(category):
    return {
        'image': ENEMY_IMAGES[category],
        'x_change': (category + 1) * difficulty,
        'y_change': (category + 1) * difficulty,
        'x_coord': randint(0, 736),
        'y_coord': randint(30, 180),
        'points': ceil((category + 1) * difficulty)
    }

def start_enemies():
    del enemies[:]
    for idx in range(num_of_enemies):
        enemy_category = randint(0, ENEMY_CATEGORIES_COUNT - 1)
        enemies.append(create_enemy(enemy_category))


def render_enemy(x, y, idx):
    screen.blit(enemies[idx]['image'], (x, y))

# Bullet
bullet_img = pygame.image.load(f'{IMAGE_PATH}/bullet.png')
bullet_y = player_y
bullet_x = player_x
bullet_y_change = 8
bullet_state = 'ready'

def render_bullet(x,y):
    global bullet_state
    bullet_state = 'fired'
    screen.blit(bullet_img, (x + 16, y + 10))

# Collisions
def is_collision(enemy_x, enemy_y, bullet_x, bullet_y, scope):
    distance = sqrt(pow(enemy_x - bullet_x, 2) + (pow(enemy_y - bullet_y, 2)))
    if distance < scope:
        return True
    
# Score
score_value = 0

SCORE_X = 10
SCORE_Y = 10

def render_score():
    score = score_font.render("Score : " + str(score_value), True, GOLDEN_COLOR)
    screen.blit(score, (SCORE_X, SCORE_Y))

# Menu
TITLE_X = 25
TITLE_Y = 210

SUBTITLE_X = 150
SUBTITLE_Y = 290

def render_menu():
    title = title_font.render('Space Invaders', True, GOLDEN_COLOR)
    screen.blit(title, (TITLE_X, TITLE_Y))

    subtitle = subtitle_font.render('Press Enter to Play', True, GOLDEN_COLOR)
    screen.blit(subtitle, (SUBTITLE_X, SUBTITLE_Y))

# Game Over
is_game_over = False

GAME_OVER_X = 140
GAME_OVER_Y = 210

RETRY_X = 130
RETRY_Y = 290

def render_game_over():
    game_over = title_font.render('Game Over', True, GOLDEN_COLOR)
    screen.blit(game_over, (GAME_OVER_X, GAME_OVER_Y))

    retry_message = subtitle_font.render('Press Enter to Retry', True, GOLDEN_COLOR)
    screen.blit(retry_message, (RETRY_X, RETRY_Y))

while True:

    clock.tick(60)

    render_background()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and not playing:
                score_value = 0
                difficulty = 1
                start_enemies()
                playing = True
            if event.key == pygame.K_LEFT:
                player_x_change = -4
            elif event.key == pygame.K_RIGHT:
                player_x_change = 4
            if event.key == pygame.K_SPACE and bullet_state == 'ready':
                bullet_sound = pygame.mixer.Sound(f'{SOUND_PATH}/laser.wav')
                bullet_sound.play()
                bullet_x = player_x
                render_bullet(bullet_x, bullet_y)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT and player_x_change < 0:
                    player_x_change = 0
            if event.key == pygame.K_RIGHT and player_x_change > 0:
                    player_x_change = 0

    if not playing:
        if is_game_over:
            render_game_over()
            render_score()
        else:
            render_menu()
    else:

        # Player Movement
        player_x += player_x_change

        if player_x <= 0:
            player_x = 0
        elif player_x >= 736:
            player_x = 736

        render_player(player_x, player_y)

        for idx in range(num_of_enemies):

            # Enemy Movement
            if enemies[idx]['x_coord'] <= 0 or enemies[idx]['x_coord'] >= 736:
                enemies[idx]['x_change'] = -enemies[idx]['x_change']
                enemies[idx]['y_coord'] += enemies[idx]['y_change']

            enemies[idx]['x_coord'] += enemies[idx]['x_change']

            # Handling Enemy-Player Collision
            player_collision = is_collision(enemies[idx]['x_coord'], enemies[idx]['y_coord'], player_x, player_y, 35)
            if player_collision:
                game_over_sound = pygame.mixer.Sound(f'{SOUND_PATH}/game_over.wav')
                game_over_sound.play()
                is_game_over = True
                playing = False
                for j in range(num_of_enemies):
                    enemies[j]['y_coord'] = 2000
                render_game_over()
                break

            # Handling Enemy-Bullet Collision
            bullet_collision = is_collision(enemies[idx]['x_coord'], enemies[idx]['y_coord'], bullet_x, bullet_y, 35)
            if bullet_collision and bullet_state == 'fired':
                explosion_sound = pygame.mixer.Sound(f'{SOUND_PATH}/explosion.wav')
                explosion_sound.play()
                if difficulty < 6:
                    difficulty = difficulty * 1.2
                else:
                    difficulty = 6
                bullet_y = player_y + 10
                bullet_state = 'ready'
                score_value += enemies[idx]['points']
                enemies[idx] = create_enemy(randint(0, ENEMY_CATEGORIES_COUNT - 1))

            render_enemy(enemies[idx]['x_coord'], enemies[idx]['y_coord'], idx)
        
        render_score()

        # Bullet Movement
        if bullet_y <= 0:
            bullet_y = player_y + 10
            bullet_state = 'ready'
        if bullet_state == "fired":
            render_bullet(bullet_x, bullet_y)
            bullet_y -= bullet_y_change

    pygame.display.flip()