import os

# Tuples
WIDTH_SCREEN = 1280
HEIGHT_SCREEN = 720
WINDOW_SIZE = (WIDTH_SCREEN, HEIGHT_SCREEN)

# environment
TITLE = "El Gato Militar"
GROUND = HEIGHT_SCREEN - 500
POINTS = 60

# Colors
GRAY                    = (100, 100, 100)
NAVY_BLUE               = ( 60,  60, 100)
WHITE                   = (255, 255, 255)
RED                     = (255,   0,   0)
GREEN                   = (  0, 255,   0)
FOREST_GREEN            = ( 31, 162,  35)
BLUE                    = (  0,   0, 255)
SKY_BLUE                = ( 39, 145, 251)
YELLOW                  = (255, 255,   0)
ORANGE                  = (255, 128,   0)
PURPLE                  = (255,   0, 255)
CYAN                    = (  0, 255, 255)
BLACK                   = (  0,   0,   0)
NEAR_BLACK              = ( 19,  15,  48)
COM_BLUE                = (233, 232, 255)
GOLD                    = (255, 215,   0)

# Paths
ROOT_PATH = os.path.dirname(__file__)
RESOURCES_PATH = os.path.join(os.path.sep, ROOT_PATH, 'resources')
SPRITES_PATH = os.path.join(os.path.sep, RESOURCES_PATH, 'sprites')
CAT_SPRITE_PATH = os.path.join(os.path.sep, SPRITES_PATH, 'cat')
BACKGROUND_PATH = os.path.join(os.path.sep, RESOURCES_PATH, 'background')
HUD_PATH = os.path.join(os.path.sep, RESOURCES_PATH, 'hud')
POWER_UP_SPRITE_PATH = os.path.join(os.path.sep, SPRITES_PATH, 'powerUp')

#Background
BACKGROUND_HOME = os.path.join(BACKGROUND_PATH, 'home.png')

# Sprites
# CAT
CAT_SPRITE_WALK = (os.path.join(CAT_SPRITE_PATH, 'cat_walk.png'), 10)
CAT_SPRITE_RUN = (os.path.join(CAT_SPRITE_PATH, 'cat_run.png'), 8)
CAT_SPRITE_SLIDE = (os.path.join(CAT_SPRITE_PATH, 'cat_slide.png'), 10)
CAT_SPRITE_JUMP = (os.path.join(CAT_SPRITE_PATH, 'cat_jump.png'), 8)
CAT_SPRITE_IDLE = (os.path.join(CAT_SPRITE_PATH, 'cat_idle.png'), 10)
CAT_SPRITE_HURT = (os.path.join(CAT_SPRITE_PATH, 'cat_hurt.png'), 10)
CAT_SPRITE_FALL = (os.path.join(CAT_SPRITE_PATH, 'cat_fall.png'), 8)
CAT_SPRITE_DEAD = (os.path.join(CAT_SPRITE_PATH, 'cat_dead.png'), 10)

# POWER-UP
POWER_UP_COIN = (os.path.join(POWER_UP_SPRITE_PATH, 'coins.png'), 1)
POWER_UP_DAMAGE = (os.path.join(POWER_UP_SPRITE_PATH, 'damage.png'), 1)

# HUD
POINTS_HUD = os.path.join(HUD_PATH, 'bar_points.png')
TIME_HUD = os.path.join(HUD_PATH, 'bar_time.png')
