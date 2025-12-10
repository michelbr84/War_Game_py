import pygame
from src.config import WHITE, BLACK, RED_COLOR, YELLOW_COLOR, WIDTH, HEIGHT
from src.managers.asset_manager import AssetManager

class Renderer:
    def __init__(self, window):
        self.window = window
        self.assets = AssetManager.get_instance()
        self.health_font = pygame.font.SysFont('comicsans', 30)
        self.winner_font = pygame.font.SysFont('comicsans', 80)

    def draw(self, red, yellow, border_rect):
        # Draw Background
        if self.assets.space_bg:
             self.window.blit(self.assets.space_bg, (0, 0))
        else:
             self.window.fill(WHITE) # Fallback

        # Draw Border
        pygame.draw.rect(self.window, BLACK, border_rect)

        # Draw Health
        red_health_text = self.health_font.render("Health: " + str(red.health), 1, WHITE)
        yellow_health_text = self.health_font.render("Health: " + str(yellow.health), 1, WHITE)
        self.window.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 10))
        self.window.blit(yellow_health_text, (10, 10))

        # Draw Spaceships
        if self.assets.yellow_spaceship:
            self.window.blit(self.assets.yellow_spaceship, (yellow.rect.x, yellow.rect.y))
        else:
            pygame.draw.rect(self.window, YELLOW_COLOR, yellow.rect) # Fallback

        if self.assets.red_spaceship:
            self.window.blit(self.assets.red_spaceship, (red.rect.x, red.rect.y))
        else:
            pygame.draw.rect(self.window, RED_COLOR, red.rect) # Fallback

        # Draw Bullets
        for bullet in red.bullets:
            pygame.draw.rect(self.window, RED_COLOR, bullet)

        for bullet in yellow.bullets:
            pygame.draw.rect(self.window, YELLOW_COLOR, bullet)

        pygame.display.update()

    def draw_winner(self, text):
        draw_text = self.winner_font.render(text, 1, WHITE)
        self.window.blit(draw_text, (WIDTH / 2 - draw_text.get_width() / 2, HEIGHT / 2 - draw_text.get_height() / 2))
        pygame.display.update()
        pygame.time.delay(5000)
