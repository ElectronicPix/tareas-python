from animal import Animal

class Perro(Animal): # Clase derivada
    def hacerSonido(self):
        print(f"{self.getNombre()} dice: ¡Guau!")