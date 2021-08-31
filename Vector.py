import math
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

    def translate(self,vetorR3):
        v_aux = VetorR3(vetorR3[0],vetorR3[1],vetorR3[2])
        # v_aux.normalize()
        self.x += v_aux.x
        self.y += v_aux.y
        if( self.z > 300):
            self.z -= v_aux.z
        else:
            self.z += v_aux.z
        
        self.normalize()