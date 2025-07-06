class Forma:
    """
    Clase base que define la "plantilla" para las formas geométricas.

    Esta clase sirve como un modelo general. Las clases que hereden de ella
    (como Circulo, Rectangulo) deben implementar sus propios métodos
    `calcularArea` y `calcularPerimetro` para que el polimorfismo funcione
    correctamente.

    Esta es una implementación "informal" de una clase base, sin usar el módulo `abc`.
    """
    def calcularArea(self):
        """Método base para calcular el área. Las subclases deben sobreescribirlo."""
        # La instrucción 'pass' no hace nada. Sirve como un marcador de posición
        # para un método que se espera que las clases hijas implementen.
        pass

    def calcularPerimetro(self):
        """Método base para calcular el perímetro. Las subclases deben sobreescribirlo."""
        pass
    
