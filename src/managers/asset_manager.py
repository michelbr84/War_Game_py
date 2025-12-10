import os
import pygame
from src.config import SPACE_SHIP_WIDTH, SPACE_SHIP_HEIGHT, WIDTH, HEIGHT

class AssetManager:
    _instance = None

    def __init__(self):
        # Base asset path
        # Assuming run from root of the project
        self.ASSETS_DIR = os.path.join(os.getcwd(), 'assets')
        
        self.yellow_spaceship = None
        self.red_spaceship = None
        self.space_bg = None
        self.bullet_hit_sound = None
        self.bullet_fire_sound = None
        
        # Initialize mixer just in case, though Game class should usually do this
        if not pygame.mixer.get_init():
             pygame.mixer.init()
        if not pygame.font.get_init():
             pygame.font.init()

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def load_assets(self):
        # Load Images
        self.yellow_spaceship = self._load_image('spaceship_yellow.png')
        self.red_spaceship = self._load_image('spaceship_red.png')
        self.space_bg = self._load_image('space.png')

        # Transform Images
        if self.yellow_spaceship:
            self.yellow_spaceship = pygame.transform.rotate(
                pygame.transform.scale(self.yellow_spaceship, (SPACE_SHIP_WIDTH, SPACE_SHIP_HEIGHT)), 90
            )
        
        if self.red_spaceship:
            self.red_spaceship = pygame.transform.rotate(
                pygame.transform.scale(self.red_spaceship, (SPACE_SHIP_WIDTH, SPACE_SHIP_HEIGHT)), -90
            )
            
        if self.space_bg:
            self.space_bg = pygame.transform.scale(self.space_bg, (WIDTH, HEIGHT))

        # Load Sounds
        self.bullet_hit_sound = self._load_sound('Grenade+1.mp3')
        self.bullet_fire_sound = self._load_sound('Gun+Silencer.mp3')

    def _load_image(self, filename):
        path = os.path.join(self.ASSETS_DIR, filename)
        if not os.path.exists(path):
            print(f"Warning: Asset not found at {path}")
            return None
        return pygame.image.load(path)

    def _load_sound(self, filename):
        path = os.path.join(self.ASSETS_DIR, filename)
        if not os.path.exists(path):
            print(f"Warning: Sound not found at {path}")
            return None
        return pygame.mixer.Sound(path)
