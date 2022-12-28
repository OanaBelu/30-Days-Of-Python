
# Project Preparation (pygame basics)

# Installing pygame :pip install pygame
# Creating a pygame window

import pygame

pygame.init()

screen = pygame.display.set_mode([640, 480])

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

main()
