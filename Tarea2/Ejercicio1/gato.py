from animal import Animal

class Gato(Animal): # Clase derivada
    def hacerSonido(self):
        print(f"{self.getNombre()} dice: ¡Miau!")