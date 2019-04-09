# Program: Jpaint
# Author: Joel Moore
# License: GPLv3
# Version: 1.5

import pygame
from pygame.locals import *

pygame.init()


def main():
    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    userColor = (0, 0, 0)
    go = True
    draw = False
    erase = False
    radius = 25
    color = blue
    (rx, ry) = (0, 25)
    (gx, gy) = (0, 60)
    (bx, by) = (0, 95)
    keepGoing2 = True
    mouseOn = False
    redX = 0
    greenX = 0
    blueX = 0
    userColor = (redX, greenX, blueX)
    pygame.mouse.set_cursor(*pygame.cursors.broken_x)

    screen = pygame.display.set_mode((1000, 1000))
    pygame.display.set_caption("Jpaint")
    screen.fill(green)
    while go == True:
        for event in pygame.event.get():

            if pygame.mouse.get_pressed() == (1, 0, 0):
                (x, y) = pygame.mouse.get_pos()
                draw = True
                pygame.draw.rect(screen, blue, (x - x % 100, y - y % 100, 100, 100))

            if pygame.mouse.get_pressed() == (0, 0, 1):
                (x, y) = pygame.mouse.get_pos()
                erase = True
                pygame.draw.rect(screen, green, (x - x % 100, y - y % 100, 100, 100))

            if pygame.mouse.get_pressed() == (0, 1, 0):
                screen.fill(white);

            if event.type == pygame.MOUSEBUTTONUP:
                draw = False
                erase = False

            if event.type == pygame.MOUSEMOTION:
                print(1)
                if draw:
                    (x, y) = pygame.mouse.get_pos()
                    pygame.draw.rect(screen, color, (x - x % 100, y - y % 100, 100, 100))

            pygame.display.flip()

            if event.type == pygame.QUIT:
                go = False


main()