class Contacto:
    """Clase que representa un contacto en una agenda telefónica.
    Atributos:
        nombre (str): Nombre completo del contacto.
        telefono (str): Número telefónico del contacto.
        email (str): Dirección de correo electrónico del contacto.
        direccion (str): Dirección física del contacto.
    """
    def __init__(self, nombre, telefono, email = '', direccion = ''):
        #Inicializa un nuevo contacto
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
        self.direccion = direccion
        
    def actualizar(self, nombre = None, telefono = None, email = None, direccion = None):
        #Actualizar los datos del contacto con los valores proporcionados
        if nombre is not None:
            self.nombre = nombre
        if telefono is not None:
            self.telefono = telefono
        if email is not None:
            self.email = email
        if direccion is not None:
            self.direccion = direccion
            
    def __str__(self):
        #Devuelve una representación en texto del contacto
        return f"Nombre: {self.nombre}\n Telefono: {self.telefono}\n Email: {self.email}\n Dirección: {self.direccion}"
