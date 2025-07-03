# Importa la clase Animal desde el módulo animal para poder heredar de ella.
from animal import Animal

# Define la clase Perro, que hereda de la clase Animal.
# Esto significa que Perro es una "subclase" de Animal y obtiene
# todos sus atributos (nombre, edad) y métodos (getNombre, comer, etc.).
class Perro(Animal): # Clase derivada
    """
    Representa un perro, un tipo específico de Animal.
    Hereda de la clase Animal.
    """
    def hacerSonido(self):
        """
        Sobrescribe el método hacerSonido de la clase base (Animal).
        En lugar del sonido genérico, imprime el ladrido específico del perro.
        """
        # Llama al método getNombre() heredado de la clase Animal para obtener
        # el nombre del perro y lo incluye en el mensaje.
        print(f"{self.getNombre()} dice: ¡Guau!")