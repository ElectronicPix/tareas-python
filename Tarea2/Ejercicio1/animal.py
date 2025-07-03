#El Reino Animal

#Objetivo: Demostrar Abstracción, Encapsulamiento y Herencia.

class Animal: # Clase base
    def __init__(self, nombre, edad):# Constructor 
        self.__nombre = nombre #privado
        self.__edad = edad #privado
        
    def getNombre(self):
        return self.__nombre
    
    def getEdad(self):
        return self.__edad
    
    def setNombre(self, nuevoNombre):
        self.__nombre = nuevoNombre
    
    def setEdad(self, nuevaEdad):
        self.__edad = nuevaEdad
    
    def hacerSonido(self):
        print("El animal hace un sonido.")

    def comer(self):
        print("El animal está comiendo.")
        