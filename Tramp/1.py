import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
screen.fill("white")
circle(screen, (255, 215, 0), (200, 175), 100)
circle(screen, (255, 0, 0), (150, 141), 22)
circle(screen, (255, 0, 0), (232, 141), 18)
circle(screen, (0, 0, 0), (150, 141), 22, 1)
circle(screen, (0, 0, 0), (232, 141), 18, 1)
circle(screen, (0, 0, 0), (150, 141), 8)
circle(screen, (0, 0, 0), (232, 141), 8)
rect(screen, (0, 0, 0), (155, 200, 70, 13))
polygon(screen, (0, 0, 0), [(100,100), (166,132),(188,132), (120,100)])
polygon(screen, (0, 0, 0), [(266,100), (191,132),(211,132), (286,100)])
pygame.display.update()
clock = pygame.time.Clock()

while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

#pygame.quit()