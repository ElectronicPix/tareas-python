"""
Script principal para demostrar el polimorfismo con diferentes formas geométricas.

Este script crea instancias de varias clases de formas (Círculo, Rectángulo),
las almacena en una lista y luego itera sobre ellas para calcular y mostrar
sus áreas y perímetros respectivos.
"""
from circulo import Circulo
from rectangulo import Rectangulo

def mostrar_calculos_formas():
    """
    Crea una lista de formas, calcula sus propiedades y las imprime en la consola.
    """
    # Se crea una lista que contiene objetos de diferentes clases (Circulo, Rectangulo),
    # pero todos heredan de la clase base 'Forma'.
    formas = [
        Circulo(radio=2),
        Rectangulo(ancho=5, alto=2)
    ]

    print("--- Calculando propiedades de las formas ---")
    # Gracias al polimorfismo, podemos llamar a los mismos métodos (calcularArea, calcularPerimetro)
    # en diferentes objetos, y Python ejecutará la implementación correcta para cada clase.
    for forma in formas:
        # Obtiene el nombre de la clase del objeto para una salida más clara.
        nombre_forma = forma.__class__.__name__
        print(f"\n--- {nombre_forma} ---")
        print(f"Área: {forma.calcularArea():.2f}")
        print(f"Perímetro: {forma.calcularPerimetro():.2f}")

# El bloque `if __name__ == '__main__':` asegura que el código dentro de él
# solo se ejecute cuando el script es el programa principal.
if __name__ == '__main__':
    mostrar_calculos_formas()
    