import pygame
import random
from settings import *

# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()


all_sprites = pygame.sprite.Group()


# Game Loop
running = True
while running:
    # Process input(event)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Update
    all_sprites.update()
    # Draw / render
    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.flip()
    # keep loop running at the right speed
    clock.tick(FPS)
