import pygame

# Window
WIDTH, HEIGHT = 1200, 600
TITLE = "Space War Game"
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED_COLOR = (255, 0, 0)
YELLOW_COLOR = (255, 255, 0)

# Gameplay
VEL = 5
BULLET_VEL = 8
MAX_BULLETS = 4
SPACE_SHIP_WIDTH, SPACE_SHIP_HEIGHT = 55, 40

# Events (Pygame User Events)
# Using pygame.USEREVENT directly might cause issues if not initialized, 
# but for constants it's standard pattern to define offsets.
YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

# Fonts
FONT_COMIC = 'comicsans'

# Shapes
BORDER = pygame.Rect(WIDTH // 2 - 5, 0, 10, HEIGHT)
