from forma import Forma

class Rectangulo(Forma):
    """
    Representa una forma geométrica de rectángulo.
    Hereda de la clase Forma y implementa sus métodos para calcular área y perímetro.
    """
    def __init__(self, ancho: float, alto: float):
        """
        Inicializa un nuevo objeto Rectangulo.

        Args:
            ancho (float): El ancho del rectángulo.
            alto (float): El alto del rectángulo.
        """
        self.ancho = ancho
        self.alto = alto
        
    def calcularArea(self):
        """
        Calcula el área del rectángulo usando la fórmula: ancho * alto.

        Returns:
            float: El área del rectángulo.
        """
        return self.ancho * self.alto
    
    def calcularPerimetro(self):
        """
        Calcula el perímetro del rectángulo usando la fórmula: 2 * (ancho + alto).

        Returns:
            float: El perímetro del rectángulo.
        """
        return 2 * (self.ancho + self.alto)
        