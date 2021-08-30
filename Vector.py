import math
class VetorR3():

    def __init__(self, px, py, pz):
        self.x = px
        self.y = py
        self.z = pz

    def normalize(self):
        norma = self.norma()
        self.x /= norma
        self.y /= norma
        self.z /= norma

    def norma(self):
        return math.sqrt(pow(self.x,2) + pow(self.y,2) + pow(self.z,2))