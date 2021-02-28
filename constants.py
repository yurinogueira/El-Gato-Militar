import os


# Tuples
WINDOW_SIZE = (1280, 720)

# Paths
ROOT_PATH = os.path.dirname(__file__)
RESOURCES_PATH = os.path.join(os.path.sep, ROOT_PATH, 'resources')
SPRITES_PATH = os.path.join(os.path.sep, RESOURCES_PATH, 'sprites')
CAT_SPRITE_PATH = os.path.join(os.path.sep, SPRITES_PATH, 'cat')

# Sprites
CAT_SPRITE_WALK = (os.path.join(CAT_SPRITE_PATH, 'cat_walk.png'), 10)
CAT_SPRITE_RUN = (os.path.join(CAT_SPRITE_PATH, 'cat_run.png'), 8)
CAT_SPRITE_SLIDE = (os.path.join(CAT_SPRITE_PATH, 'cat_slide.png'), 10)
CAT_SPRITE_JUMP = (os.path.join(CAT_SPRITE_PATH, 'cat_jump.png'), 8)
CAT_SPRITE_IDLE = (os.path.join(CAT_SPRITE_PATH, 'cat_idle.png'), 10)
CAT_SPRITE_HURT = (os.path.join(CAT_SPRITE_PATH, 'cat_hurt.png'), 10)
CAT_SPRITE_FALL = (os.path.join(CAT_SPRITE_PATH, 'cat_fall.png'), 8)
CAT_SPRITE_DEAD = (os.path.join(CAT_SPRITE_PATH, 'cat_dead.png'), 10)
