# Area de un Rectangulo 

class Restangulo: #clase 
    #método constructor
    def __init__(self, base, altura):
        #atributos
        self.base = base
        self.altura = altura
        
    def area(self):#poner self deltro de los parentesis
        return self.base * self.altura
    
r = Restangulo(4, 5)
print("Area del rectangulo: ", r.area())
