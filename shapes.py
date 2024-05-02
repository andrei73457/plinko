import pygame as pg
import pymunk.pygame_util
from random import randrange
pymunk.pygame_util.positive_y_is_up = False


RES = WIDTH, HEIGHT = 1200,750
ball_mass, ball_radius = 1, 7
segment_thickness = 2
x1, x4 = 10, WIDTH - 10
y1 = 100

def create_ball(space):
    ball_moment = pymunk.moment_for_circle(ball_mass, 0, ball_radius)
    ball_body = pymunk.Body(ball_mass, ball_moment)
    ball_body.position = randrange(WIDTH//2 -5, WIDTH//2 +5), 30
    ball_shape = pymunk.Circle(ball_body, ball_radius)
    ball_shape.elasticity = .5
    ball_shape.friction = 0.5
    space.add(ball_body, ball_shape)
    return ball_body

def create_segment(from_, to_, thickness, space, color):
    segment_shape = pymunk.Segment(space.static_body, from_, to_, thickness)
    segment_shape.color = pg.color.THECOLORS[color]
    space.add(segment_shape)


def create_peg(x, y, space, color):
    circle_shape = pymunk.Circle(space.static_body, radius=10, offset=(x, y))
    circle_shape.color = pg.color.THECOLORS[color]
    circle_shape.elasticity = 0.1
    circle_shape.friction = 0.5
    space.add(circle_shape)


x2, x3 = WIDTH // 2 - 18, WIDTH // 2 + 18
y2, y3, y4, y5 = HEIGHT // 4 - 40, HEIGHT // 4, HEIGHT // 2 - 1.5 * 100, HEIGHT - 4 * 100
L1, L2, L3, L4 = (x1, -100), (x1, y1), (x2, y2), (x2, y3)
R1, R2, R3, R4 = (x4, -100), (x4, y1), (x3, y2), (x3, y3)
platforms = (L1, L2), (L2, L3), (L3, L4), (R1, R2), (R2, R3), (R3, R4)
