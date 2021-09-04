import math
import pygame

def matriz_rot(axis, angle):
    rad = math.pi * angle/180
    if axis == 'x':
        return [
            [1, 0, 0],
            [0, math.cos(rad), -math.sin(rad)],
            [0, math.sin(rad), math.cos(rad)]
        ]

    elif axis == 'y':
        return [
            [math.cos(rad), 0, -math.sin(rad)],
            [0, 1, 0],
            [math.sin(rad), 0, math.cos(rad)]
        ]

    elif axis == 'z':
        return [
            [math.cos(rad), -math.sin(rad), 0],
            [math.sin(rad), math.cos(rad), 0],
            [0, 0, 1]
        ]

class VetorR3():

    def __init__(self, px, py, pz):
        self.x = float(px)
        self.y = float(py)
        self.z = float(pz)

    def normalize(self):
        norma = self.norma()
        # print(norma)
        self.x /= norma
        self.y /= norma
        self.z /= norma

    def norma(self):
        return round(math.sqrt(pow(self.x,2) + pow(self.y,2) + pow(self.z,2))+1)

    def values(self):
        return [self.x, self.y, self.z]

    def rotate(self, axis, angle):

        matriz_aux = matriz_rot(axis, angle)
        point = self.values()
        aux = [0,0,0]
        for i in range(len(matriz_aux)):
            line = matriz_aux[i]
            for j in range(3):
                aux[i] += line[j]*point[j]
        
        self.x = aux[0]
        self.y = aux[1]
        self.z = aux[2]

    def inverse(self):
        return VetorR3(-self.x, -self.y, -self.z)

class Point():
    tempo = 10
    pixeis = []
    for pixel in pixeis:
        pixel.fill((100,100,100))

    def __init__(self, px, py, pz, color):
        self.x = float(px)
        self.y = float(py)
        self.z = float(pz)
        self.dx = 0
        self.dy = 0
        self.dz = 0
        self.color = color
        self.pixel_size = 2
    
    def values(self):
        return [self.x, self.y, self.z]
 
    def rotate(self, axis, angle):
        matriz_aux = matriz_rot(axis, angle)
        point = self.values()
        aux = [0,0,0]
        for i in range(len(matriz_aux)):
            line = matriz_aux[i]
            for j in range(3):
                aux[i] += line[j]*point[j]
        
        self.x = aux[0]
        self.y = aux[1]
        self.z = aux[2]

    def get_color(self):
        return self.color

    def scale(self, size):
        self.x *= size
        self.y *= size
        self.z *= size

    def update(self):
        if abs(self.dx - self.x) > 0 or abs(self.dz - self.z) > 0 or  abs(self.dy - self.y) > 0:
            dis_x = abs(self.dx - self.x)/self.tempo
            dis_y = abs(self.dy - self.y)/self.tempo
            norma =  math.sqrt(pow(dis_x,2) + pow(dis_y,2))

            if self.dx > self.x:
                self.dx -= dis_x * dis_x / norma
            elif self.dx < self.x:
                self.dx += dis_x * dis_x / norma

            if self.dy > self.y:
                self.dy -= dis_y * dis_y/norma
            elif self.dy < self.y:
                self.dy += dis_y * dis_y/norma

    def draw(self,width,height):
        pixel = self.pixeis[self.pixel_size - 1]
        pixel.fill(self.get_color())
        window = pygame.display.get_surface()
        # window.blit(pixel, (self.dx + width/2, self.dy + height/2))
        window.blit(pixel, (self.x + width/2, self.y + height/2))

class Graph():

    def __init__(self, points):
        self.points = points
        self.x_rotation = 0

    def rotate(self,axis,angle):
        if axis == 'x':
            self.x_rotation += angle
            for point in self.points:
                point.rotate(axis,angle)
                
        elif axis == 'z':
            for point in self.points:
                point.rotate('x',-self.x_rotation)
                point.rotate(axis, angle)
                point.rotate('x', self.x_rotation)

    def scale(self, size):
        if size == 0:
            return 
        for point in self.points:
            point.scale(size)