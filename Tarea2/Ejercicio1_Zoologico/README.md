# 📁 1. Estructura del Proyecto
<pre><code>zoologico/
├── animal.py       # Clase base abstracta Animal
├── perro.py        # Clase derivada Perro
├── gato.py         # Clase derivada Gato
└── main.py         # Programa principal (punto de entrada)<pre></code>

# 🐍 2. Requisitos

Python 3

# 💻 3. Instrucciones para Ejecutar
Abre una terminal o consola y navega a la carpeta zoologico:
```bash
cd zoologico
```python main.py
# Ejecuta el programa:
```bash
python main.py      
```

# 📝 4. Descripción del Código
El código define una jerarquía de clases para representar animales en un zoológico. La clase base `Animal` es abstracta y define un método abstracto `hacer_sonido`. Las clases derivadas `Perro` y `Gato` implementan este método con sonidos específicos. El programa principal crea instancias de estas clases y llama a sus métodos para mostrar los sonidos que hacen.
# 🐶 5. Detalles de Implementación
- **animal.py**: Define la clase abstracta `Animal` con un método abstracto `hacer_sonido`.
- **perro.py**: Implementa la clase `Perro` que hereda de   `Animal` y define el método `hacer_sonido` para devolver "Guau!".
- **gato.py**: Implementa la clase `Gato` que hereda de `Animal` y define el método `hacer_sonido` para devolver "Miau!".
- **main.py**: Crea instancias de `Perro` y `Gato`, y llama a sus métodos `hacer_sonido` para imprimir los sonidos que hacen.
# 🐱 6. Ejemplo de Uso      
```python
from perro import Perro             
from gato import Gato
def main():
    # Crear instancias de Perro y Gato
    mi_perro = Perro("Rex")
    mi_gato = Gato("Miau")

    # Llamar al método hacer_sonido
    print(f"{mi_perro.nombre} dice: {mi_perro.hacer_sonido()}")
    print(f"{mi_gato.nombre} dice: {mi_gato.hacer_sonido()}")

if __name__ == "__main__":
    main()