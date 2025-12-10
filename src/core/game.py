import pygame
from src.config import WIDTH, HEIGHT, TITLE, FPS, SPACE_SHIP_WIDTH, SPACE_SHIP_HEIGHT, BORDER, RED_HIT, YELLOW_HIT, MAX_BULLETS
from src.managers.asset_manager import AssetManager
from src.entities.spaceship import Spaceship
from src.systems.collision import CollisionSystem
from src.ui.renderer import Renderer

class Game:
    def __init__(self):
        # Initialize Pygame
        pygame.init()
        pygame.font.init()
        pygame.mixer.init()

        # Setup Window
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        
        # Load Assets
        self.assets = AssetManager.get_instance()
        self.assets.load_assets()
        
        # Setup Core Components
        self.clock = pygame.time.Clock()
        self.renderer = Renderer(self.window)
        
        # Game State
        self.running = True
        self.red = Spaceship(700, 300, 'red')
        self.yellow = Spaceship(100, 300, 'yellow')
        
    def handle_input(self):
        keys_pressed = pygame.key.get_pressed()
        self.yellow.move_yellow(keys_pressed, BORDER)
        self.red.move_red(keys_pressed, BORDER)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(self.yellow.bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(
                        self.yellow.rect.x + self.yellow.rect.width, 
                        self.yellow.rect.y + self.yellow.rect.height // 2 - 2, 
                        10, 5
                    )
                    self.yellow.bullets.append(bullet)
                    if self.assets.bullet_fire_sound:
                        self.assets.bullet_fire_sound.play()

                if event.key == pygame.K_RCTRL and len(self.red.bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(
                        self.red.rect.x, 
                        self.red.rect.y + self.red.rect.height // 2 - 2, 
                        10, 5
                    )
                    self.red.bullets.append(bullet)
                    if self.assets.bullet_fire_sound:
                        self.assets.bullet_fire_sound.play()

            if event.type == RED_HIT:
                self.red.health -= 1
                if self.assets.bullet_hit_sound:
                    self.assets.bullet_hit_sound.play()

            if event.type == YELLOW_HIT:
                self.yellow.health -= 1
                if self.assets.bullet_hit_sound:
                    self.assets.bullet_hit_sound.play()

    def check_winner(self):
        winner_text = ""
        if self.red.health <= 0:
            winner_text = "Yellow Wins!"
        if self.yellow.health <= 0:
            winner_text = "Red Wins!"

        if winner_text != "":
            self.renderer.draw_winner(winner_text)
            self.running = False

    def run(self):
        print("Starting Game Loop...")
        while self.running:
            self.clock.tick(FPS)
            self.handle_events()
            self.handle_input()
            CollisionSystem.handle_bullets(self.yellow, self.red)
            self.renderer.draw(self.red, self.yellow, BORDER)
            self.check_winner()

        pygame.quit()
