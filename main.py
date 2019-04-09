# Program: Jpaint
# Author: Joel Moore
# License: GPLv3
# Version: 1.5

import pygame
from pygame.locals import *
from planet import Planet, Water, People
pygame.init()


def main():
    planet = Planet()
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
    sSize = 50
    screen = pygame.display.set_mode((1000, 1000))
    screen.fill(green)
    while go == True:
        for event in pygame.event.get():
            if (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_w):
                    color = blue
                elif (event.key == pygame.K_p):
                    color = red
                elif (event.key == pygame.K_u):
                    old = planet.people
                    planet.update()
                    for i in range(len(old), len(planet.people)):
                        print(planet.people[i].x, planet.people[i].y)
                        print((planet.people[i].x * sSize, planet.people[i].y * sSize, sSize, sSize))
                        pygame.draw.rect(screen, red, (planet.people[i].x * sSize, planet.people[i].y * sSize, sSize, sSize))

            if pygame.mouse.get_pressed() == (1, 0, 0):
                (x, y) = pygame.mouse.get_pos()
                draw = True
                pygame.draw.rect(screen, color, (x - x % sSize, y - y % sSize, sSize, sSize))
                if (color == blue):
                    planet.add(Water(x // sSize, y // sSize))
                else:
                    planet.add(People(x // sSize, y // sSize))


            if pygame.mouse.get_pressed() == (0, 0, 1):
                (x, y) = pygame.mouse.get_pos()
                erase = True
                pygame.draw.rect(screen, green, (x - x % sSize, y - y % sSize, sSize, sSize))

            if pygame.mouse.get_pressed() == (0, 1, 0):
                screen.fill(white)

            if event.type == pygame.MOUSEBUTTONUP:
                draw = False
                erase = False

            if event.type == pygame.MOUSEMOTION:
                print(1)
                if draw:
                    (x, y) = pygame.mouse.get_pos()
                    pygame.draw.rect(screen, color, (x - x % sSize, y - y % sSize, sSize, sSize))

            pygame.display.flip()

            if event.type == pygame.QUIT:
                go = False


main()