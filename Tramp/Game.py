import pygame
from pygame.draw import *
from random import randint

pygame.init()
pygame.display.set_caption("УБИЙЦА ШАРОВ and Kybow 3000")
B = [0, 0, 0]
FPS = 1
screen = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
points = 0
courier = pygame.font.SysFont("courier", 36)


def new_ball():
    global x, y, r
    '''рисует новый шарик '''
    x = randint(100, 1100)
    y = randint(100, 760)
    r = randint(22, 100)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)
    circle(screen, BLACK, (x, y), r, 1)


def new_polygon():
    global x, y, r
    x = randint(100, 1100)
    y = randint(100, 760)
    r = randint(22, 100)
    color = COLORS[randint(0, 5)]
    rect(screen, color,  (x, y, r, r))
    rect(screen, BLACK,  (x, y, r, r), 1)


def click(event):
    global points
    print(x, y, r)
    if (event.pos[1] - y) ** 2 + (event.pos[0] - x) ** 2 <= r ** 2:
        print('+')
        points += 1
    else:
        print('-')
        points = 0


def rand():
    r = randint(0, 1)
    if r==0:
        new_polygon()
    else:
        new_ball()

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    screen.fill("#FFDAB9")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click(event)
            #print(points)

    pygame.draw.rect(screen, B, [1, 1, 1200, 900], 11)
    text_total = courier.render(f"Score: {points}", 0, BLACK)
    screen.blit(text_total, (30, 30))
    rand()
    pygame.display.update()

pygame.quit()
