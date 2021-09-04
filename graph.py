import pygame
from Geometric import *
import numpy as np
import random
import os

from multiprocessing import Pool as ThreadPool
if __name__ == '__main__':
    amount_of_cores = os.cpu_count()
    pool = ThreadPool(amount_of_cores)

    pygame.init()
    height = 600
    width = 600

    clock = pygame.time.Clock()

    pixel_max_size = 4
    Point.pixeis = [pygame.Surface((x+1,x+1)) for x in range(pixel_max_size+1)]

    font = pygame.font.SysFont("Arial", 20)

    window = pygame.display.set_mode((width,height))

##### For the use of multiprocessing
def multiprocess_rotate(points):
    if __name__ == '__main__':
        equation_points.points = pool.map(rotate_point, points)    

def rotate_point(args):
    if args[1][1] != 0:
        args[0].rotate('x', args[1][1])
    if args[1][2] != 0:
        args[0].rotate('y', args[1][2])
    if args[1][0] != 0:
        args[0].rotate('z', args[1][0])
    return args[0]

def update_point(point):
    point.update()
    return point
####

def axis(vetor,color):
    points = []
    for pos in range(100):
        points.append(Point(vetor[0]* pos, vetor[1] * pos, vetor[2] * pos, color))
    return points

def donut(graph,raio): ## Pontos não pode ser vazio
    fx = lambda t,s : raio * math.cos(t) + raio/2 * math.cos(s) * math.cos(t)
    fy = lambda t,s : raio * math.sin(t) + raio/2 * math.cos(s) * math.sin(t)
    fz = lambda t,s : raio/2 * math.sin(s)
    new_format(graph,fx,fy,fz,np.arange(0,2* math.pi, 0.05),np.arange(-math.pi, math.pi, 0.1))

def ampulheta(graph,raio): ## Pontos não pode ser vazio
    fx = lambda t,s : raio * s * math.cos(t)
    fy = lambda t,s : raio * s * math.sin(t)
    fz = lambda t,s : raio * s
    new_format(graph,fx,fy,fz,np.arange(0,2* math.pi, 0.05),np.arange(-math.pi, math.pi, 0.1))

def esfera(graph,raio):
    fx = lambda t,s : raio * math.cos(t) * math.sin(s)
    fy = lambda t,s : raio * math.sin(t) * math.sin(s)
    fz = lambda t,s : raio * math.cos(s)
    new_format(graph,fx,fy,fz,np.arange(0,2* math.pi, 0.05),np.arange(0, math.pi, 0.1))

def new_format(graph,fx,fy,fz,t_range,s_range):
    pontos = graph.points
    counter = 0
    for t in t_range:
        for s in s_range:
            if counter >= len(pontos):
                pontos.append(Point(0,0,0,pontos[0].color))
            pontos[counter].x = fx(t,s)
            pontos[counter].y = fy(t,s)
            pontos[counter].z = fz(t,s)
            counter += 1
    graph.points = pontos[:counter]

def generate_points(quantity,color):
    points = []
    for _ in range(quantity):
        points.append(Point(0,0,0,color))
    return points

def Setup():
    OX_COLOR = (255,0,0)
    OY_COLOR = (0,255,0)
    OZ_COLOR = (0,0,255)
    global main_axis, equation_points, OX, OY, OZ
    OX = Graph(axis((1,0,0),OX_COLOR))
    OY = Graph(axis((0,-1,0),OY_COLOR))
    OZ = Graph(axis((0,0,1),OZ_COLOR))
    main_axis = [OX, OY, OZ]

    # point_colors = (
    #     lambda self : (
    #         int((abs(self.dx) / (width/256)))%256,
    #         int((abs(self.dy) / (height/256)))%256,
    #         140)
    #     )
    # point_colors = (lambda self: (100,100,100))

    equation_points = Graph(generate_points(7397,(100,100,100)))

    # ampulheta(equation_points,40)
    # esfera(equation_points,40)
    donut(equation_points,40)

    # equation_points.rotate('x', 60)
    # equation_points.rotate('z', 60)
    # for ax in main_axis:
    #     ax.rotate('x', 60)
    #     ax.rotate('z', 60)
    # equation_points.scale(4)
    return

def Input():
    events = pygame.event.get()
    scalation = 1.0
    mouse_buttons = pygame.mouse.get_pressed(num_buttons = 5)
    keys = pygame.key.get_pressed()
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
            
            if __name__ == '__main__':
                inversed_relative_as_pressed = relative_as_pressed + [0]
                inversed_relative_as_pressed[1] = -inversed_relative_as_pressed[1]
                points = zip(equation_points.points,[inversed_relative_as_pressed for _ in range(len(equation_points.points))])
                multiprocess_rotate(points)           

            for a in main_axis:
                a.rotate('x', -relative_as_pressed[1])
                a.rotate('z', relative_as_pressed[0])

        
    if keys[pygame.K_UP]:
        scalation = scalation + 0.25 
        equation_points.scale(scalation)

    if keys[pygame.K_DOWN]:
        scalation = scalation - 0.25 
        equation_points.scale(scalation)

    return (1 in [keys[pygame.K_DOWN],keys[pygame.K_UP]] or 1 in mouse_buttons)

def Logic():
    ### Por algum motivo desconhecido, fazer multiprocess do update é 10x pior que o map
    # if __name__ == '__main__':
    #     equation_points.points = pool.map(update_point, equation_points.points)
    ######
    equation_points.points = list(map(update_point,equation_points.points))
    multiprocess_rotate(zip(equation_points.points,[[1,1,0] for _ in range(len(equation_points.points))]))
    return

def Fps():
    global font
    font_surface = font.render(str(int(clock.get_fps())), True, (200,200,200))
    window.blit(font_surface, [0, 0])

def Draw():
    window.fill((0,0,0))
    
    ordem_print = sorted(
        equation_points.points + 
        OX.points + 
        OY.points + 
        OZ.points, 
        key = lambda item : item.z)
    
    depth = 1
    max_depth = len(ordem_print)
    for point in ordem_print:
        point.pixel_size = int(depth / (max_depth/pixel_max_size)) + 1
        point.draw(width,height)
        depth += 1

    Fps()
    return

asd = 0
if __name__ == '__main__':
    Setup()
    while(1):

        # if asd % 300 == 0:
        #     esfera(equation_points,4*40)
        # elif asd % 200 == 0:
        #     donut(equation_points,4*40)
        # elif asd % 100 == 0:
        #     ampulheta(equation_points,40)
        # asd += 1

        Input()
        Logic()
        Draw()

        pygame.display.update()
        clock.tick(60)


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