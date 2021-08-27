import pygame
from pygame import Surface
from pygame import Rect
import time
import math
import random

window = pygame.display.set_mode((500,500))

def circle_form(x,y,r):
    result = pow((x-r),2) + pow((y-r),2)
    if (result) > pow(r,2)-100 and result < pow(r,2)+100:
        return True
    else:
        return False

def plot_circle(window, precision=1):
    point = pygame.Surface((1,1))
    point.fill((255,0,0))
    size_map = 500 * precision
    translate = size_map/2
    for x in range(size_map):
        for y in range(size_map):
            if circle_form(x,y,translate):
                window.blit(point,(x,y))

def circle_form_around(x,r,pos_x,pos_y,window):
    first = pow(r,2) - pow((x-(pos_x)),2)
    if(first>=0):
        result = math.sqrt(first)
        return(pos_y+result,pos_y-result)
    else:
        return (-1,-1)

def plot_circle_around(window,position,radius, color = (255,0,0), to_fill = False):
    point = pygame.Surface((1,1))
    point.fill(color)
    size_map = 500
    for x in range(size_map):
        (plus,minus) = circle_form_around(x,radius,position[0],position[1],window)
        if to_fill:
            for i in range(int(minus),int(plus),2):
                if i > 0:
                    window.blit(point,(x,i))
        else:
            if plus > 0 : 
                window.blit(point,(x,plus))
            if minus > 0:
                window.blit(point,(x,minus))
        


radius = 100
color = (255,0,0)
filler = False
while(1):
    # window.fill((0,0,0))

    pos = pygame.mouse.get_pos()
    pygame.event.get()

    button = pygame.mouse.get_pressed(num_buttons=5)
    if button [0]: #esquerdo
        can_draw = True
    else:
        can_draw = False

    if button [1]:#meio
        color = (random.randint(0,255) ,random.randint(0,255),random.randint(0,255))
    elif button [2] and pygame.MOUSEBUTTONDOWN: # direito
        filler = not(filler)
    elif button[4]: #botao lateral
        radius += 1
    elif button[3]:#botao lateral
        if radius >0:
            radius -= 1

    if(can_draw):
        plot_circle_around(window,pos,radius,color,filler)

    # plot_circle(window,1)
    pygame.display.update()
    # time.sleep(1)

