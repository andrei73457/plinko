import pygame as pg
import pymunk.pygame_util
from random import randrange
pymunk.pygame_util.positive_y_is_up = False
from time import sleep

from shapes import create_ball, create_peg, create_segment, platforms

RES = WIDTH, HEIGHT = 1200,750
FPS = 60

pg.init()
surface = pg.display.set_mode(RES)
clock = pg.time.Clock()
draw_options = pymunk.pygame_util.DrawOptions(surface)

space = pymunk.Space()
space.gravity = 0, 2000
ball_mass, ball_radius = 1, 7
segment_thickness = 2

a, b, c, d = 10, 100, 18, 40
x1, x2, x3, x4 = a, WIDTH // 2 - c, WIDTH // 2 + c, WIDTH - a
y1, y2, y3, y4, y5 = b, HEIGHT // 4 - d, HEIGHT // 4, HEIGHT // 2 - 1.5 * b, HEIGHT - 4 * b

#for platform in platforms:
#   create_segment(*platform, segment_thickness, space, 'darkolivegreen')




"""
for n in range(9):
    x = WIDTH//2
    h = 100
    step = 60
    h2 = 50 * n
    z = 1
    print(h2)
    for m in range(z):
        z += 2
        x2 = -1.5 * step if m % 2 else -step
        create_peg(x + x2, h + h2, space, 'darkslateblue')
"""
#create_peg(peg_x, peg_y, space, 'darkslateblue')

peg_y, step = y4, 60
for i in range(10):
    peg_x = -1.5 * step if i % 2 else -step
    for j in range(WIDTH // step + 2):
        create_peg(peg_x, peg_y, space, 'darkslateblue')
        if i == 9:
            create_segment((peg_x, peg_y+ 50), (peg_x, HEIGHT), segment_thickness, space, 'darkslategray')
        peg_x += step
    peg_y += .5 * step
"""
# pegs
peg_y, step = y4, 60
for i in range(10):
    peg_x = -1.5 * step if i % 2 else -step
    for j in range(WIDTH // step + 2):
        create_peg(peg_x, peg_y, space, 'darkslateblue')
        if i == 9:
            create_segment((peg_x, peg_y + 50), (peg_x, HEIGHT), segment_thickness, space, 'darkslategray')
        peg_x += step
    peg_y += 0.5 * step

"""

create_segment((0, HEIGHT), (WIDTH, HEIGHT), 20, space, 'darkslategray')
balls = []
dt = 0
while True:
    surface.fill(pg.Color('black'))

    for i in pg.event.get():
        if i.type == pg.QUIT:
            exit()

    space.step(1 / FPS)
    space.debug_draw(draw_options)

    # [pg.draw.circle(surface, color, ball.position, ball_radius) for color, ball in balls]
    dt += 1/FPS
    if dt > 1:
        dt = 0
        balls.append(((randrange(256), randrange(256), randrange(256)), create_ball(space)))

    for color, ball in balls:
        pg.draw.circle(surface, color, (int(ball.position[0]), int(ball.position[1])), ball_radius)
    
    pg.display.flip()
    clock.tick(FPS)