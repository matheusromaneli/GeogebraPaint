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
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            OX.rotate('x', 1)
            OY.rotate('x', 1)
            OZ.rotate('x', 1)

        if keys[pygame.K_DOWN]:
            OX.rotate('x', -1)
            OY.rotate('x', -1)
            OZ.rotate('x', -1)

        if keys[pygame.K_LEFT]:
            OX.rotate('y', -1)
            OY.rotate('y', -1)
            OZ.rotate('y', -1)

        if keys[pygame.K_RIGHT]:
            OX.rotate('y', 1)
            OY.rotate('y', 1)
            OZ.rotate('y', 1)

    return

def Logic():
    return

def Draw():
    window.fill((0,0,0))
    vetores = [(OX,(255,0,0)), (OZ, (0,0,255)), (OY, (0,255,0))]
    ordem_print = sorted(vetores, key = lambda item : item[0].z)
    for vetor in ordem_print:
        reta((width/2,height/2), vetor[0], vetor[1])
    pygame.display.update()
    return

Setup()
while(1):
    Input()
    Logic()
    Draw()