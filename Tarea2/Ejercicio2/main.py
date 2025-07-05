from circulo import Circulo
from rectangulo import Rectangulo

class Main:
    def forma(self):
        formas = [Circulo(2), Rectangulo(5, 2)]
        for forma in formas:
            print(f"Area {forma.calcularArea()}")
            print(f"Perimetro {forma.calcularPerimetro()}")
            
        
        
if __name__ == '__main__':
    main = Main()
    main.forma()
    