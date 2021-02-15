import pygame

LIME = (0, 255, 0)
WHITE = (255, 255, 255)

class Snake(pygame.sprite.Sprite):

    def __init__(self, color, width, height):

        # Initialize parent class
        super().__init__()

        # Create snake's body
        self.image = pygame.Surface([width, height])
        self.image.fill(LIME)
        self.image.set_colorkey(WHITE)

        # Draw snake on the screen
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # Get snake's dimensions
        self.rect = self.image.get_rect()

    def moveLeft(self, pixels):
        self.rect.x -= pixels

    def moveRight(self, pixels):
        self.rect.x += pixels

    def moveDown(self, pixels):
        self.rect.y += pixels

    def moveUp(self, pixels):
        self.rect.y -= pixels