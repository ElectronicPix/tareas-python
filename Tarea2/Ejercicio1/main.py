# Importa las clases Perro y Gato desde sus respectivos archivos
from perro import Perro
from gato import Gato

# Clase principal para ejecutar el programa
class Main:
    def principal(self):
        # Crea una instancia de Perro
        perro = Perro("Docky", 4)
        # Crea una instancia de Gato
        gato = Gato("Lucas", 6)
        
        # Muestra información y acciones del perro
        print(f"Nombre del perro: {perro.getNombre()}, Edad: {perro.getEdad()}")
        perro.hacerSonido()
        perro.comer()

        # Muestra información y acciones del gato
        print(f"Nombre del gato: {gato.getNombre()}, Edad: {gato.getEdad()}")
        gato.hacerSonido()
        gato.comer()
        
        print()
        
        # Lista de animales para demostrar polimorfismo
        animales = [perro, gato]
        for animal in animales:
            # Llama al método hacerSonido de cada animal
            animal.hacerSonido()
            
            print()
        
# Punto de entrada del programa
if __name__ == "__main__":
    main = Main()
    main.principal()