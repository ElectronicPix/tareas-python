'''
Ejercicio 1: Definir una Clase 
1. Define una clase llamada Animal.
2. Agrega un constructor __init__ que reciba los atributos Raza y Genero.
3. Define un método llamado informacion que imprima el tipo de animal y genero.
4. Instancia un objeto de la clase Animal y utiliza sus atributos y métodos fuera de la clase.
'''

class Animal(): # definimos la clase
    #métodos
    def __init__(self, Raza, Genero):#contructor de la clase
        #atributos
        self.Raza = Raza
        self.Genero = Genero
    
    def Informacion(self):
        print(f"el animal es de tipo {self.Raza} y  genero {self.Genero}")
        
#Instanciar un objeto de la clase Animal

miAnimal = Animal('Pastor Alemán', 'canis')
miAnimal.Informacion()