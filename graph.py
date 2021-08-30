import pygame
from Vector import VetorR3
height = 600
width = 600

window = pygame.display.set_mode((width,height))

def reta(ponto, vetor, color):
    aux_p = [ponto[0], ponto[1]]
    pencil = pygame.Surface((3,3))
    pencil.fill(color)
    if not(vetor.x != 0 or vetor.z != 0):
        window.blit(pencil,aux_p)
        return
    for i in range(int(ponto[0]), int(width),1):
        #desenha em aux_p
        window.blit(pencil, aux_p)
        aux_p[0] += vetor.x
        aux_p[1] -= vetor.z
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
        #se o botao[0] estiver pressionado:
            #pego a angulação do vetor antigo e o novo
            #rotaciono os vetores OX, OZ, OZ
        print(event)
    return

def Logic():
    return

def Draw():
    window.fill((0,0,0))
    reta((width/2,height/2), OX, (255,0,0))
    reta((width/2,height/2), OZ, (0,0,255))
    reta((width/2,height/2), OY, (0,255,0))
    pygame.display.update()
    return

Setup()
while(1):
    Input()
    Logic()
    Draw()