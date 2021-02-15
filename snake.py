import pygame

LIME = (0, 255, 0)
WHITE = (255, 255, 255)

# Screen dimensions
SCREEN_LENGTH = 840
SCREEN_HEIGHT = 720

SCREEN_LENGTH_MID = SCREEN_LENGTH // 2
SCREEN_HEIGHT_MID = SCREEN_HEIGHT // 2

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

        if self.rect.x < 0:
            self.rect.x = 0

    def moveRight(self, pixels):
        self.rect.x += pixels

        if self.rect.x > SCREEN_LENGTH - 20:
            self.rect.x = SCREEN_LENGTH - 20

    def moveDown(self, pixels):
        self.rect.y += pixels

        if self.rect.y > SCREEN_HEIGHT - 20:
            self.rect.y = SCREEN_HEIGHT - 20

    def moveUp(self, pixels):
        self.rect.y -= pixels

        if self.rect.y < 0:
            self.rect.y = 0