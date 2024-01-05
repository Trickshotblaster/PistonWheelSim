#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      s-bhoener
#
# Created:     03/01/2024
# Copyright:   (c) s-bhoener 2024
# Licence:     MIT
#-------------------------------------------------------------------------------

# make piston and wheel thingy

import pygame
import math
import time
bg_color = (50, 50, 50)

screen = pygame.display.set_mode((600, 600))

pygame.display.set_caption('Piston and wheel')

screen.fill(bg_color)

running = True

centerpos = (300, 300)
radius = 35
length = 200
t = 0
ct = time.time()
speed = 10
while running:
    # wheel
    screen.fill(bg_color)
    pygame.draw.circle(screen, (255, 255, 255), centerpos, radius)

    # position of a
    ax = radius * math.cos(t)
    ay = radius * math.sin(t)
    # draw a
    pygame.draw.circle(screen, (0,0,0), (centerpos[0] + int(ax), centerpos[1] + int(ay)), 5)


    # position of b
    # ay = side 1
    # length = hypotenuse
    # solving for side 2
    # a^2 + b^2 = c^2 -> b = sqrt(c^2 - a^2)
    bx = math.sqrt(length**2 - ay**2) + ax
    by = 0
    # draw b
    pygame.draw.circle(screen, (0,0,0), (centerpos[0] + int(bx), centerpos[1] + by), 5)

    # draw line
    pygame.draw.line(screen, (50, 50, 200), (centerpos[0]+ax, centerpos[1]+ay), (centerpos[0]+bx, centerpos[1]+by))

    # update time
    t += (time.time() - ct) * speed
    ct = time.time()

    # draw info
    pygame.font.init()
    font = pygame.font.Font(None, 14)
    infostring1 = 'ax: ' + str(int(ax)) + ", ay: " + str(int(ay))
    text1 = font.render(infostring1, True, (255, 255, 255), (0, 0, 0))

    textRect1 = text1.get_rect()
    textRect1.center = (50, 10)

    screen.blit(text1, textRect1)

    infostring2 = "bx: " + str(int(bx)) + ", by: " + str(int(by))
    text2 = font.render(infostring2, True, (255, 255, 255), (0, 0, 0))

    textRect2 = text2.get_rect()
    textRect2.center = (50, 30)

    screen.blit(text2, textRect2)

    # update logic
    pygame.display.update()
    pass
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
