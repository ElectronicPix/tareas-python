from forma import Forma

class Rectangulo(Forma):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
    def calcularArea(self):
        return self.ancho * self.alto
    
    def calcularPerimetro(self):
        return 2 * (self.ancho + self.alto)
        