
"""Project

For the graduation project we're going to be building the classic video game Snake using a third party library c
alled pygame.

Today's project is particularly large so there are two project posts for today.

The first is going to be a project preparation post which will walk you through everything you need to know about
pygame. The second will contain a walkthrough for the entire project, and will also contain the project brief."""

import pygame
import pygame.display

WINDOW_HEIGHT = 840
WINDOW_WIDTH = 800
WINDOW_DIMENSIONS = WINDOW_WIDTH, WINDOW_HEIGHT

pygame.init()
pygame.display.set_caption("Snake")

clock = pygame.time.Clock()
screen = pygame.display.set_mode(WINDOW_DIMENSIONS)

def play_game():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        clock.tick(30)

play_game()
