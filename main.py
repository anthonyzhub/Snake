#! /usr/bin/python3

import pygame
from snake import Snake
from fruit import Fruit

# Colors
BLACK = (0, 0, 0)
LIME = (0, 255, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Screen dimensions
SCREEN_LENGTH = 840
SCREEN_HEIGHT = 720

SCREEN_LENGTH_MID = SCREEN_LENGTH // 2
SCREEN_HEIGHT_MID = SCREEN_HEIGHT // 2

def updateScreen(screen, clock, allSpritesList):

    # OBJECTIVE: Update screen 

    # Turn screen black
    screen.fill(BLACK)

    # Draw sprites
    allSpritesList.draw(screen)

    # Update screen
    pygame.display.flip()

    # FPS
    clock.tick(60)

def snakeMovements(keysPressed, snake):

    if keysPressed[pygame.K_UP]:
        snake.moveUp(5)
    
    if keysPressed[pygame.K_DOWN]:
        snake.moveDown(5)

    if keysPressed[pygame.K_LEFT]:
        snake.moveLeft(5)

    if keysPressed[pygame.K_RIGHT]:
        snake.moveRight(5)

if __name__ == "__main__":
    
    # Initialize pygame
    pygame.init()

    # Create a window
    screen = pygame.display.set_mode((SCREEN_LENGTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Anthony's Snake Game")

    # Create snake sprite
    snake = Snake(LIME, 15, 15)
    snake.rect.x = SCREEN_LENGTH_MID
    snake.rect.y = SCREEN_HEIGHT_MID

    # Create fruit sprite
    fruit = Fruit(RED, 15, 15)
    fruit.randomPosition() # <= NOTE: Generate random X & Y position for fruit

    # Add all sprites to list
    allSpritesList = pygame.sprite.Group()
    allSpritesList.add(snake)
    allSpritesList.add(fruit)

    # Create boolean variable to stop/start game
    continueGame = True

    # Initialize pygame's clock
    clock = pygame.time.Clock()

    while continueGame:

        # Look for keyboard inputs
        for event in pygame.event.get():

            # True, when "close window" button is closed
            if event.type == pygame.QUIT: 
                continueGame = False

        # Get keys pressed
        keysPressed = pygame.key.get_pressed()
        snakeMovements(keysPressed, snake)

        # Update all sprites
        allSpritesList.update()

        # Update screen
        updateScreen(screen, clock, allSpritesList)

    # Quit pygame
    pygame.quit()