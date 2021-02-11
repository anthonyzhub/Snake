#! /usr/bin/python3

import pygame

# Screen dimensions
SCREEN_LENGTH = 840
SCREEN_HEIGHT = 720

if __name__ == "__main__":
    
    # Initialize pygame
    pygame.init()

    # Create a window
    screen = pygame.display.set_mode((SCREEN_LENGTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Anthony's Snake Game")
    
    # Quit pygame
    pygame.quit()