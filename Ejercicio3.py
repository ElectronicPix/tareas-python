'''
Ejercicio 3: Crear una Clase con Múltiples Métodos
1. Define una clase llamada Calculadora.
2. Agrega un constructor que inicialice un atributo resultado en 0.
3. Define métodos para sumar, restar y mostrar el resultado.
4. Instancia un objeto de la clase Calculadora y utiliza sus métodos para realizar operaciones y mostrar el resultado final
'''

class calculadora(): #definimos la clase
    #metodos
    def __init__(self, num1, num2):
        #atributos
        self.num1 = num1
        self.num2 = num2
        self.resultado = 0
    def sumar(self):
        self.resultado = self.num1 + self.num2
        
    def restar(self):
            self.resultado = self.num1 - self.num2
        
    def mostrarResultado(self):
        print(f"el resultado es {self.resultado}")
        
miCalculadora = calculadora(2,3)
miCalculadora.sumar()
miCalculadora.mostrarResultado()
miCalculadora.restar()
miCalculadora.mostrarResultado()

