#Ej. Modelando una cafetera

class Cafetera: #clase inicia con letra mayuscula
    #definimios métod constructor
    def __init__(self, marca, capacidad):
        #atributos
        self.marca = marca
        self.capacidad = capacidad
    
    def servir_cafe(self):
        print('Sirviendo cafe caliente ☕')

mi_cafetera = Cafetera('Oster', 1.5)
print(mi_cafetera.marca) #acceso al atributo
mi_cafetera.servir_cafe() # acceso al método

mi_cafetera2 = Cafetera('BD', 2.0)
print(mi_cafetera2.capacidad)