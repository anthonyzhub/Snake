import pygame
from random import randint

RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Screen dimensions
SCREEN_LENGTH = 840
SCREEN_HEIGHT = 720

SCREEN_LENGTH_MID = SCREEN_LENGTH // 2
SCREEN_HEIGHT_MID = SCREEN_HEIGHT // 2

class Fruit(pygame.sprite.Sprite):

    def __init__(self, color, width, height):

        # Initialize super class
        super().__init__()

        # Create sprite
        self.image = pygame.Surface([width, height])
        self.image.fill(RED)
        self.image.set_colorkey(WHITE)

        # Draw sprite
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # Get sprite's dimensions
        self.rect = self.image.get_rect()

    def randomPosition(self):

        self.rect.x = randint(0, SCREEN_LENGTH-20)
        self.rect.y = randint(11, SCREEN_HEIGHT-20)