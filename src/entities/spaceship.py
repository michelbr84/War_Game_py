import pygame
from src.config import VEL, WIDTH, HEIGHT, BORDER, SPACE_SHIP_WIDTH, SPACE_SHIP_HEIGHT

class Spaceship:
    def __init__(self, x, y, color_code):
        self.rect = pygame.Rect(x, y, SPACE_SHIP_WIDTH, SPACE_SHIP_HEIGHT)
        self.color_code = color_code # 'yellow' or 'red'
        self.bullets = []
        self.health = 5

    def move_yellow(self, key_pressed, border_rect):
        if key_pressed[pygame.K_a] and self.rect.x - VEL > 0:  # left
            self.rect.x -= VEL
        if key_pressed[pygame.K_d] and self.rect.x + VEL + self.rect.width < border_rect.x:  # right
            self.rect.x += VEL
        if key_pressed[pygame.K_w] and self.rect.y - VEL > 0:  # up
            self.rect.y -= VEL
        if key_pressed[pygame.K_s] and self.rect.y + VEL + self.rect.height < HEIGHT - 15:  # down
            self.rect.y += VEL

    def move_red(self, key_pressed, border_rect):
        if key_pressed[pygame.K_LEFT] and self.rect.x - VEL > border_rect.x + border_rect.width:  # left
            self.rect.x -= VEL
        if key_pressed[pygame.K_RIGHT] and self.rect.x + VEL + self.rect.width < WIDTH:  # right
            self.rect.x += VEL
        if key_pressed[pygame.K_UP] and self.rect.y - VEL > 0:  # up
            self.rect.y -= VEL
        if key_pressed[pygame.K_DOWN] and self.rect.y + VEL + self.rect.height < HEIGHT - 15:  # down
            self.rect.y += VEL
