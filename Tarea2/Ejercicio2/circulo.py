from forma import Forma
import math


class Circulo(Forma):
    def __init__(self, radio):
        self.radio = radio
    
    def calcularArea(self):
        return math.pi * pow (self.radio, 2)
    
    def calcularPerimetro(self):
        return 2 * math.pi * self.radio