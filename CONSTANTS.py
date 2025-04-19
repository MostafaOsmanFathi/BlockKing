# Screen Configurations
SCREEN_HEIGHT = 800
SCREEN_WIDTH = 1000

# Cell Configurations
SQUARE_COLOR = "gray"
SQUARE_SCALE = 2

# Grid Dimensions
N_CELLS = 15
M_CELLS = 17
FIXED_MARGIN = 10
SQUARE_SIZE = 20 * SQUARE_SCALE
START_X = (-SCREEN_HEIGHT / 2) + 20
START_Y = 350

# Player configurations
PLAYER_SHAPE = 'square'
PLAYER_SCALE = SQUARE_SCALE - .5
# Movemnts          0:right   1:left   2:down  3:up
PLAYER_MOVEMENTS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# Game Manger configurations
UPDATE_RATE = 0.25
