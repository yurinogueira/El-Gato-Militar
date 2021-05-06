import os

import pygame.transform

from PPlay.sound import Sound

# Tuples
WIDTH_SCREEN = 1280
WIDTH_DIV = WIDTH_SCREEN / 2
HEIGHT_SCREEN = 720
HEIGHT_DIV = HEIGHT_SCREEN / 2
WINDOW_SIZE = (WIDTH_SCREEN, HEIGHT_SCREEN)

# environment
TITLE = "El Gato Militar"
GROUND = HEIGHT_SCREEN - 400
POINTS = 20
TIME = 60
JUMP_MAX = 150
SPEED = 200
GENERATED_POINTS = 40
ENEMY_PLANE_FIRST_POSITION = (400, 50)
ENEMY_PLANE_SECCOND_POSITION = (400, 150)
ENEMY_PLANE_THREE_POSITION = (400, 500)
ENEMY_PLANE_FOUR_POSITION = (400, 550)

# Colors
WHITE = (255, 255, 255)
FOREST_GREEN = (31, 162, 35)
SKY_BLUE = (39, 145, 251)
ORANGE = (255, 128, 0)
PURPLE = (255, 0, 255)
BLACK = (0, 0, 0)
NEAR_BLACK = (19, 15, 48)
COM_BLUE = (233, 232, 255)
GOLD = (255, 215, 0)
GOLDEN = (230, 89, 35)

# Paths
ROOT_PATH = os.path.dirname(__file__)
RESOURCES_PATH = os.path.join(os.path.sep, ROOT_PATH, 'resources')
SPRITES_PATH = os.path.join(os.path.sep, RESOURCES_PATH, 'sprites')
SOUND_PATH = os.path.join(os.path.sep, RESOURCES_PATH, 'sounds')
HISTORY_PATH = os.path.join(os.path.sep, RESOURCES_PATH, 'history')

CAT_SPRITE_PATH = os.path.join(os.path.sep, SPRITES_PATH, 'cat')
AIRPLANE_SPRITE_PATH = os.path.join(os.path.sep, SPRITES_PATH, 'airplanes')
ENEMY_SPRITE_PATH = os.path.join(os.path.sep, SPRITES_PATH, 'enemy')

BACKGROUND_PATH = os.path.join(os.path.sep, RESOURCES_PATH, 'background')
HUD_PATH = os.path.join(os.path.sep, RESOURCES_PATH, 'hud')
HUD_SPRITE_PATH = os.path.join(os.path.sep, SPRITES_PATH, 'hud')
POWER_UP_SPRITE_PATH = os.path.join(os.path.sep, SPRITES_PATH, 'powerUp')
BULLET_SPRITE_PATH = os.path.join(os.path.sep, SPRITES_PATH, 'bullets')
CAR_PATH = os.path.join(os.path.sep, SPRITES_PATH, 'car')

# Background
BACKGROUND_HOME = os.path.join(BACKGROUND_PATH, 'home.png')
BACKGROUND_BATTLE1 = os.path.join(BACKGROUND_PATH, 'battle1.png')
BACKGROUND_DESERT = os.path.join(BACKGROUND_PATH, 'desert.png')
BACKGROUND_SPACE = os.path.join(BACKGROUND_PATH, 'space.jpeg')
BACKGROUND_WAR = os.path.join(BACKGROUND_PATH, 'war.png')
BACKGROUND_CITY = os.path.join(BACKGROUND_PATH, 'city.png')
BACKGROUND_HISTORY = os.path.join(BACKGROUND_PATH, 'history.png')

# Sprites
BLACK_HOLE = (os.path.join(os.path.sep, SPRITES_PATH, 'black-hole.png'), 4)
EXPLOSION = (os.path.join(os.path.sep, SPRITES_PATH, 'explosion.png'), 5)
RIGHT_ARROW = (os.path.join(SPRITES_PATH, 'rightArrow.png'), 1)
LEFT_ARROW = (os.path.join(SPRITES_PATH, 'leftArrow.png'), 1)

# CAT
CAT_SPRITE_WALK = (os.path.join(CAT_SPRITE_PATH, 'cat_walk.png'), 10)
CAT_SPRITE_WALK_FLIPED = (os.path.join(CAT_SPRITE_PATH, 'cat_walk_fliped.png'), 10)
CAT_SPRITE_JUMP = (os.path.join(CAT_SPRITE_PATH, 'cat_jump.png'), 8)
CAT_SPRITE_JUMP_FLIPED = (os.path.join(CAT_SPRITE_PATH, 'cat_jump_fliped.png'), 8)
CAT_SPRITE_FALL = (os.path.join(CAT_SPRITE_PATH, 'cat_fall.png'), 8)
CAT_SPRITE_FALL_FLIPED = (os.path.join(CAT_SPRITE_PATH, 'cat_fall_fliped.png'), 8)
CAT_SPRITE_IDLE = (os.path.join(CAT_SPRITE_PATH, 'cat_idle.png'), 10)
CAT_SPRITE_IDLE_FLIPED = (os.path.join(CAT_SPRITE_PATH, 'cat_idle_fliped.png'), 10)
CAT_SPRITE_HURT = (os.path.join(CAT_SPRITE_PATH, 'cat_hurt.png'), 10)
CAT_SPRITE_DEAD = (os.path.join(CAT_SPRITE_PATH, 'cat_dead.png'), 10)

# Enemy
PLUS_JET_ENEMY_RED_FLY = (os.path.join(ENEMY_SPRITE_PATH, 'plusjet_red_fly.png'), 2)
PLUS_JET_ENEMY_PINK_FLY = (os.path.join(ENEMY_SPRITE_PATH, 'plusjet_pink_fly.png'), 2)
PLUS_JET_ENEMY_YELLOW_FLY = (os.path.join(ENEMY_SPRITE_PATH, 'plusjet_yellow_fly.png'), 2)
PLUS_JET_ENEMY_GREEN_FLY = (os.path.join(ENEMY_SPRITE_PATH, 'plusjet_green_fly.png'), 2)

#HISTORY
HISTORY_1 = os.path.join(HISTORY_PATH, '1.jpg')
HISTORY_2 = os.path.join(HISTORY_PATH, '2.jpg')
HISTORY_3 = os.path.join(HISTORY_PATH, '3.jpg')
HISTORY_4 = os.path.join(HISTORY_PATH, '4.jpg')
HISTORY_5 = os.path.join(HISTORY_PATH, '5.jpg')


# Sprites
# AIRPLANE
JET_BLUE_FLY = (os.path.join(AIRPLANE_SPRITE_PATH, 'jet_blue_fly.png'), 2)
JET_GREEN_FLY = (os.path.join(AIRPLANE_SPRITE_PATH, 'jet_green_fly.png'), 2)
JET_YELLOW_FLY = (os.path.join(AIRPLANE_SPRITE_PATH, 'jet_yellow_fly.png'), 2)
PLANE_PINK_FLY = (os.path.join(AIRPLANE_SPRITE_PATH, 'plane_pink_fly.png'), 2)

# BULLET
FIRE_BALL = (os.path.join(BULLET_SPRITE_PATH, 'fire_ball.png'), 1)
FIRE_BALL_REVERSE = (os.path.join(BULLET_SPRITE_PATH, 'fire_ball_reverse.png'), 1)
FIRE_BALL_BLUE = (os.path.join(BULLET_SPRITE_PATH, 'fire_ball_blue.png'), 1)
FIRE_BALL_PINK = (os.path.join(BULLET_SPRITE_PATH, 'fire_ball_pink.png'), 1)
TORPEDO = (os.path.join(BULLET_SPRITE_PATH, 'torpedo.png'), 3)
TORPEDO_BLACK = (os.path.join(BULLET_SPRITE_PATH, 'torpedo_black.png'), 3)

# POWER-UP
POWER_UP_COIN = (os.path.join(POWER_UP_SPRITE_PATH, 'coins.png'), 1)
POWER_UP_LIFE = (os.path.join(POWER_UP_SPRITE_PATH, 'life.png'), 1)
POWER_UP_ENERGY = (os.path.join(POWER_UP_SPRITE_PATH, 'energy.png'), 1)

#CAR
CAR_1 = (os.path.join(CAR_PATH, 'car1.png'), 1)
CAR_2 = (os.path.join(CAR_PATH, 'car2.png'), 1)
CAR_3 = (os.path.join(CAR_PATH, 'car3.png'), 1)
CAR_4 = (os.path.join(CAR_PATH, 'car4.png'), 1)
CAR_5 = (os.path.join(CAR_PATH, 'car5.png'), 1)

# HUD
SOUND_BACKGROUND = os.path.join(HUD_PATH, 'bar_empty.png')
SOUND_ENABLE = os.path.join(HUD_PATH, 'sound_enable.png')
SOUND_DISABLED = os.path.join(HUD_PATH, 'sound_disabled.png')
POINTS_HUD = os.path.join(HUD_PATH, 'bar_points.png')
TIME_HUD = os.path.join(HUD_PATH, 'bar_time.png')
LIFE_HUD = os.path.join(HUD_PATH, 'bar_life.png')
LIFE_HUD_ENEMY = os.path.join(HUD_PATH, 'bar_life_enemy.png')
SPECIAL_HUD = os.path.join(HUD_PATH, 'bar_special.png')
PAUSE_HUD = os.path.join(HUD_PATH, 'button_pause.png')
SHOP_HUD = os.path.join(HUD_PATH, 'button_shop.png')
NORMAL_BUTTON = os.path.join(HUD_PATH, 'normal_button.png')
ACTIVED_BUTTON = os.path.join(HUD_PATH, 'active_button.png')
HOVER_BUTTON = os.path.join(HUD_PATH, 'hover_button.png')
PAUSE_SCREEN = os.path.join(HUD_PATH, 'pause_screen.png')
SHOP_SCREEN = os.path.join(HUD_PATH, 'shop_screen.png')

LIFE_POINTS = (os.path.join(HUD_SPRITE_PATH, 'life_value.png'), 5)
LIFE_POINTS_ENEMY = (os.path.join(HUD_SPRITE_PATH, 'life_value_enemy.png'), 5)
SPECIAL_POINTS = (os.path.join(HUD_SPRITE_PATH, 'special_value.png'), 5)

BLUE_FIRE_SHOP = os.path.join(HUD_PATH, 'blue_fire_shop.png')
BLUE_FIRE_SHOP_B = os.path.join(HUD_PATH, 'blue_fire_shop_b.png')
PINK_FIRE_SHOP = os.path.join(HUD_PATH, 'pink_fire_shop.png')
PINK_FIRE_SHOP_B = os.path.join(HUD_PATH, 'pink_fire_shop_b.png')
TORPEDO_SHOP = os.path.join(HUD_PATH, 'torpedo_shop.png')
TORPEDO_SHOP_B = os.path.join(HUD_PATH, 'torpedo_shop_b.png')
TORPEDO_BLACK_SHOP = os.path.join(HUD_PATH, 'torpedo_black_shop.png')
TORPEDO_BLACK_SHOP_B = os.path.join(HUD_PATH, 'torpedo_black_shop_b.png')

# SOUNDS
COIN_SOUND = Sound(os.path.join(SOUND_PATH, 'coin_pickup.ogg'))
PLANE_LASER_SHOTS = Sound(os.path.join(SOUND_PATH, 'plane_shoot.ogg'))
BUTTON_SOUND = Sound(os.path.join(SOUND_PATH, 'button.ogg'))

MENU_LOOP_SOUND = Sound(os.path.join(SOUND_PATH, 'menu_loop_sound.ogg'))
SIMPLE_BATTLE_SOUND = Sound(os.path.join(SOUND_PATH, 'simple_battle_music.ogg'))
DOUBLE_BATTLE_SOUND = Sound(os.path.join(SOUND_PATH, 'double_battle_music.ogg'))
MEGA_BATTLE_MUSIC = Sound(os.path.join(SOUND_PATH, 'mega_battle_music.ogg'))
