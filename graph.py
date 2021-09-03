import pygame
from Geometric import *
import numpy as np
import random

pygame.init()
height = 600
width = 600

window = pygame.display.set_mode((width,height))

def axis(vetor):
    points = []
    for pos in range(100):
        points.append(Point(vetor[0]* pos, vetor[1] * pos, vetor[2] * pos))
    return points


def generate_points(raio):
    points = []
    for t in np.arange(0,2* math.pi, 0.05):
        for s in np.arange(-math.pi, math.pi, 0.1):
            x = raio * math.cos(t) + raio/2 * math.cos(s) * math.cos(t)
            y = raio * math.sin(t) + raio/2 * math.cos(s) * math.sin(t)
            z = raio/2 * math.sin(s)
            points.append(Point(x,y,z))
    return points

def Setup():
    global main_axis, equation_points, OX, OY, OZ
    OX = Graph(axis((1,0,0)))
    OY = Graph(axis((0,-1,0)))
    OZ = Graph(axis((0,0,1)))
    main_axis = [OX, OY, OZ]
    equation_points = Graph(generate_points(40))
    return

def Input():
    events = pygame.event.get()
    scalation = 1.0
    mouse_buttons = pygame.mouse.get_pressed(num_buttons = 5)
    for event in events:
        mouse_pos = pygame.mouse.get_pos()
        button_pressed_in = (0,0)
        rel = pygame.mouse.get_rel()
        
        if event == pygame.MOUSEBUTTONDOWN:
            button_pressed_in = pygame.mouse.get_pos()
        
        if mouse_buttons[0]:
            relative_as_pressed = [mouse_pos[0] - button_pressed_in[0], mouse_pos[1] - button_pressed_in[1]]
            
            norma_relative = math.sqrt(relative_as_pressed[0] **2 + relative_as_pressed[1]**2)
            relative_as_pressed[0] /= norma_relative
            relative_as_pressed[1] /= norma_relative

            if rel[0] != 0:
                relative_as_pressed[0] *= -rel[0]
            if rel[1] != 0:
                relative_as_pressed[1] *= rel[1]
            
            equation_points.rotate('x', -relative_as_pressed[1])
            equation_points.rotate('z', relative_as_pressed[0])
            for axis in main_axis:
                axis.rotate('x', -relative_as_pressed[1])
                axis.rotate('z', relative_as_pressed[0])
        
    if mouse_buttons[3]:
        scalation = scalation + 0.25 
        equation_points.scale(scalation)

    if mouse_buttons[4]:
        scalation = scalation - 0.25 
        equation_points.scale(scalation)

    return

def Logic():
    return

def Draw():
    window.fill((0,0,0))
    pixel = pygame.Surface((2,2))
    OX_COLOR = (255,0,0)
    OY_COLOR = (0,255,0)
    OZ_COLOR = (0,0,255)
    
    ordem_print = sorted(
        equation_points.to_draw((100,100,100)) + 
        OX.to_draw(OX_COLOR) + 
        OY.to_draw(OY_COLOR) + 
        OZ.to_draw(OZ_COLOR), 
        key = lambda item : item[0].z)

    for point in ordem_print:
        pixel.fill(point[1])
        window.blit(pixel, (point[0].x+ width/2, point[0].y+height/2))
    pygame.display.update()
    return

Setup()
while(1):
    Input()
    Logic()
    Draw()


## PARA PEGAR AS SETAS:
# keys = pygame.key.get_pressed()
#     if keys[pygame.K_UP]:
#         for item in vectors:
#             item[0].rotate('x', -1)
#         equation_points.rotate('x', -1)

#     if keys[pygame.K_DOWN]:
#         for item in vectors:
#             item[0].rotate('x', 1)
#         equation_points.rotate('x', 1)

#     if keys[pygame.K_LEFT]:
#         for item in vectors:
#             item[0].rotate('y', -1)
#         equation_points.rotate('y', -1)

#     if keys[pygame.K_RIGHT]:
#         for item in vectors:
#             item[0].rotate('y', 1)
#         equation_points.rotate('y', 1)

## PARA MANTER RODANDO EM Logic()
# axis = ['x', 'y', 'z']
# equation_points.rotate('x', 1)
# equation_points.rotate('y', 1)
# equation_points.rotate('z', 1)
# for item in vectors:
#     item[0].rotate('x', 1)
#     item[0].rotate('y', 1)
#     item[0].rotate('z', 1)