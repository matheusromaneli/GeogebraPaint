import pygame
from Geometric import *
import numpy as np
import random

height = 600
width = 600

window = pygame.display.set_mode((width,height))

def reta(ponto, vetor, color, weight = (3,3)):
    aux_p = [ponto[0], ponto[1]]
    pencil = pygame.Surface(weight)
    pencil.fill(color)
    if not(vetor.x != 0 or vetor.y != 0):
        window.blit(pencil,aux_p)
        return
    vetor_aux = VetorR3(vetor.x,vetor.y,vetor.z)
    vetor_aux.normalize()
    for i in range(200):
        #desenha em aux_p
        window.blit(pencil, aux_p)
        aux_p[0] += vetor_aux.x
        aux_p[1] += vetor_aux.y
    return

def generate_points(raio):
    points = []
    for t in np.arange(0,2* math.pi, 0.05):
        for s in np.arange(-math.pi/2, math.pi/2, 0.05):
            x = raio * math.cosh(s) * math.cos(t)
            y = raio * math.cosh(s) * math.sin(t)
            z = raio * math.sinh(s)
            points.append(Point(x,y,z))
    return points

def Setup():
    global vectors, equation_points
    vectors = [
        (VetorR3(1,0,0), (255,0,0))
        ,(VetorR3(0,1,0), (0,255,0))
        ,(VetorR3(0,0,1), (0,0,255)) 
        # ,(VetorR3(1,1,1), (200,200,200))
    ]

    equation_points = Graph(generate_points(40))
    return

def Input():
    events = pygame.event.get()
    for event in events:
        # print( event)
        mouse_buttons = pygame.mouse.get_pressed()
        mouse_pos = pygame.mouse.get_pos()
        button_pressed_in = (0,0)
        rel = pygame.mouse.get_rel()
        # rel = (1,1)
        if event == pygame.MOUSEBUTTONDOWN:
            button_pressed_in = pygame.mouse.get_pos()
        if mouse_buttons[0]:
            relative_as_pressed = [mouse_pos[0] - button_pressed_in[0], mouse_pos[1] - button_pressed_in[1]]
            
            norma_relative = math.sqrt(relative_as_pressed[0] **2 + relative_as_pressed[1]**2)
            relative_as_pressed[0] /= norma_relative
            relative_as_pressed[1] /= norma_relative

            if rel[0] != 0:
                relative_as_pressed[0] *= rel[0]
            if rel[1] != 0:
                relative_as_pressed[1] *= rel[1]
            
            equation_points.rotate('x', relative_as_pressed[1])
            equation_points.rotate('y', relative_as_pressed[0])
            for item in vectors:
                item[0].rotate('x', relative_as_pressed[1])
                item[0].rotate('y', relative_as_pressed[0])
        
    return

def Logic():
    return

def Draw():
    window.fill((0,0,0))
    ordem_print = sorted(vectors, key = lambda item : item[0].z)
    pixel = pygame.Surface((1,1))
    for vetor in ordem_print:
        reta((width/2,height/2), vetor[0], vetor[1])

    for point in equation_points.points:
        pixel.fill((abs(point.x),abs(point.y),abs(point.z)))
        window.blit(pixel, (point.x+ width/2, point.y+height/2))
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