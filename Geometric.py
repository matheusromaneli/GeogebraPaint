import math

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

    def __init__(self, px, py, pz):
        self.x = float(px)
        self.y = float(py)
        self.z = float(pz)
    
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

class Graph():

    def __init__(self, points):
        self.points = points
        self.x_rotation = 0

    def rotate(self,axis,angle):
        if axis == 'x':
            if self.x_rotation + angle > 90:
                return
            self.x_rotation += angle
            for point in self.points:
                point.rotate(axis,angle)
        elif axis == 'z':
            for point in self.points:
                point.rotate('x',-self.x_rotation)
                point.rotate(axis, angle)
                point.rotate('x', self.x_rotation)

    def to_draw(self, color):
        array = map(lambda point: (point, color), self.points)
        return list(array)
        