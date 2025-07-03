from perro import Perro
from gato import Gato

class Main:
    def principal(self):
        perro = Perro("Docky", 4)
        gato = Gato("Lucas", 6)
        
        print(f"Nombre del perro: {perro.getNombre()}, Edad: {perro.getEdad()}")
        perro.hacerSonido()
        perro.comer()

        print(f"Nombre del gato: {gato.getNombre()}, Edad: {gato.getEdad()}")
        gato.hacerSonido()
        gato.comer()
        
        print()
        
        animales = [perro, gato]
        for animal in animales:
            animal.hacerSonido()
            
            print()
        
if __name__ == "__main__":
    main = Main()
    main.principal()