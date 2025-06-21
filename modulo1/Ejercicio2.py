'''
Ejercicio 2: Trabajar con Atributos y Métodos
1. Define una clase llamada Coche.
2. Agrega un atributo marca y un método acelerar que imprima un mensaje indicando que el coche está acelerando.
3. Instancia un objeto de la clase Coche y modifica el atributo marca fuera de la clase.
4. Llama al método acelerar desde fuera de la clase.
'''

class Coche(): #definimos la clase
    #métodos
    def __init__(self, marca):
        #atributos
        self.marca = marca
        
    def acelerar(self):
        print("El conche está acelerando")
        
#Instanciamos un objeto de la clase coche
miCoche = Coche('Mazda')
print(miCoche.marca)

# Modificamos el atributo marca fuera de la clase
miCoche.marca = 'Toyota'
print(miCoche.marca)

miCoche.acelerar()