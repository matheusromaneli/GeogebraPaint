import pygame
from Vector import VetorR3
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
        aux_p[1] -= vetor_aux.y
    return

def Setup():
    global OX, OY, OZ
    OX = VetorR3(1,0,0)
    OY = VetorR3(0,1,0)
    OZ = VetorR3(0,0,1)
    return

def Input():
    events = pygame.event.get()
    for event in events:
        # print( event)
        mouse_buttons = pygame.mouse.get_pressed()
        mouse_pos = pygame.mouse.get_pos()
        rel = pygame.mouse.get_rel()
        # rel = (1,1)
        if mouse_buttons[0]:
            center_vet = [mouse_pos[0]-width/2 ,mouse_pos[1]- height/2]
            # center_vet = rel
            OX.translate((center_vet[1],center_vet[0],0))
            OY.translate((center_vet[0],-center_vet[1],0))
            OZ.translate((0,-center_vet[1], 0))

    return

def Logic():
    return

def Draw():
    window.fill((0,0,0))
    reta((width/2,height/2), OX, (255,0,0), (7,7))
    reta((width/2,height/2), OZ, (0,0,255), (6,6))
    reta((width/2,height/2), OY, (0,255,0), (5,5))
    pygame.display.update()
    return

Setup()
while(1):
    Input()
    Logic()
    Draw()