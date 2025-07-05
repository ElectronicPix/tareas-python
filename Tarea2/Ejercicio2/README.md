# 🧮 Calculadora de Formas Geométricas

Este proyecto demuestra los principios de **abstracción** y **polimorfismo** usando una jerarquía de clases para formas geométricas. Se pueden calcular áreas y perímetros de círculos y rectángulos.

## 🧱 Estructura del Proyecto
<pre><code>
formas_geometricas/
├── forma.py # Clase abstracta Forma
├── circulo.py # Clase concreta Circulo
├── rectangulo.py # Clase concreta Rectangulo
├── main.py # Programa principal
└── README.md # Instrucciones de uso </code></pre>


## 🚀 Cómo Ejecutar

### ✅ Requisitos

- Python 3.6 o superior
- No requiere bibliotecas externas

### ▶️ Instrucciones

1. Clona el repositorio o descarga los archivos.
2. Abre una terminal y navega a la carpeta `formas_geometricas`.
3. Ejecuta:

```bash
python main.py

# 📌 Resultado Esperado
Se mostrará por consola el área y el perímetro de cada forma, demostrando el uso de polimorfismo al invocar métodos concretos de subclases a través de referencias del tipo Forma.

