import pygame
from src.config import BULLET_VEL, WIDTH, YELLOW_HIT, RED_HIT

class CollisionSystem:
    @staticmethod
    def handle_bullets(yellow, red):
        """
        Manages bullet movement and collision detection.
        :param yellow: Yellow Spaceship instance
        :param red: Red Spaceship instance
        """
        # Handle Yellow Bullets
        for bullet in yellow.bullets:
            bullet.x += BULLET_VEL
            if red.rect.colliderect(bullet):
                pygame.event.post(pygame.event.Event(RED_HIT))
                yellow.bullets.remove(bullet)
            elif bullet.x > WIDTH:
                yellow.bullets.remove(bullet)

        # Handle Red Bullets
        for bullet in red.bullets:
            bullet.x -= BULLET_VEL
            if yellow.rect.colliderect(bullet):
                pygame.event.post(pygame.event.Event(YELLOW_HIT))
                red.bullets.remove(bullet)
            elif bullet.x < 0:
                red.bullets.remove(bullet)
