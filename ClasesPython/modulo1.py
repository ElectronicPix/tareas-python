#Ejemplo procedimental 
def saludar(nombre):
    print(f"Hola, {nombre}")
    
saludar('juan')

#Programación orientada a objetos
#Agregar atributos(propiedades) - variables
class Persona(object): #Crear la clase, palabra object ya no es necesaria
    #pass
    #metodo - se identifican con self + parametros
    def __init__(self, nombre, edad): #constructor de la clase
        #atributos - propiedades usando self
        self.nombre = nombre
        self.edad = edad
    
    def saludar(self):
        print(f"Hola, {self.nombre}, tienes {self.edad} años.")

#Instanciar un Objeto de la clase persona.
#objeto es una variable, porque se instancia
p1 = Persona('juan', 30) #tipo de la clase persona, tiene el objeto persona
#Llamar al método saludar del objeto p1
p1.saludar()

p2 = Persona('Ana', 25)
#Llamar al método saludar del objeto p2
p2.saludar() #acceso al metodo