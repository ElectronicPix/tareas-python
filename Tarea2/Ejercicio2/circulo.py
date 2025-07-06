from forma import Forma
import math


class Circulo(Forma):
    """
    Representa una forma geométrica de círculo.
    Hereda de la clase Forma y implementa sus métodos para calcular área y perímetro.
    """
    def __init__(self, radio: float):
        """
        Inicializa un nuevo objeto Círculo.

        Args:
            radio (float): El radio del círculo.
        """
        self.radio = radio
    
    def calcularArea(self):
        """
        Calcula el área del círculo usando la fórmula: π * radio^2.

        Returns:
            float: El área del círculo.
        """
        return math.pi * (self.radio ** 2)
    
    def calcularPerimetro(self):
        """
        Calcula el perímetro (circunferencia) del círculo usando la fórmula: 2 * π * radio.

        Returns:
            float: El perímetro del círculo.
        """
        return 2 * math.pi * self.radio