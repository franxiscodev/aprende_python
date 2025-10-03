# 🐍 Aprende Python - Laboratorio de Aprendizaje

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-en%20desarrollo-orange)

**Un proyecto estructurado para aprender Python de manera organizada y práctica.**

## 🎯 Objetivo

Este proyecto sirve como un laboratorio personal para aprender y experimentar con Python, organizando ejemplos, ejercicios y proyectos por temas específicos.

## 📁 Estructura del Proyecto

```bash
aprende_python/
├── 📂 fundamentos/           # Conceptos básicos de Python
├── 📂 estructuras_datos/     # Estructuras y validación de datos  
├── 📂 programacion_funcional/ # Programación funcional
├── 📂 poo/                   # Programación Orientada a Objetos
├── 📂 manejo_archivos/       # Manejo de archivos y formatos
├── 📂 tests/                 # Pruebas automatizadas
├── 📂 holapython/            # Ejemplos iniciales y hello world
├── 📜 main.py                # Punto de entrada principal
├── 📜 requirements.txt       # Dependencias del proyecto
└── 📜 README.md              # Este archivo
```


## 🚀 Comenzar

### Prerrequisitos
- Python 3.8 o superior
- Git
- pip (gestor de paquetes de Python)

### Instalación

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/tu-usuario/aprende_python.git
   cd aprende_python

## Configurar entorno virtual
python -m venv .venv

# Linux/macOS
source .venv/bin/activate

# Windows
.venv\Scripts\activate

## Instalar dependencias
pip install -r requirements.txt

## Ejecutar el proyecto
python main.py

## 📚 Módulos de Aprendizaje

### 🔰 Fundamentos
- Variables y tipos de datos
- Estructuras de control
- Funciones
- List comprehensions

### 🏗️ Estructuras de Datos
- Listas, tuplas, diccionarios
- Sets y frozensets
- Dataclasses
- Pydantic (validación de datos)

### 🔄 Programación Funcional
- Lambdas y funciones anónimas
- Map, filter, reduce
- Generadores
- Decoradores

### 🧭 POO (Programación Orientada a Objetos)
- Clases y objetos
- Herencia y polimorfismo
- Métodos especiales
- Encapsulamiento

### 💾 Manejo de Archivos
- Archivos de texto
- JSON y CSV
- Gestión de rutas
- Serialización

## 🛠️ Desarrollo

### Comandos útiles
```bash
# Ejecutar tests
pytest

# Formatear código
black .

# Verificar tipos
mypy .

# Verificar estilo de código
flake8 .

📝 Convenciones de commits
feat: Nueva característica

fix: Corrección de bug

docs: Cambios en documentación

style: Cambios de formato (sin afectar funcionalidad)

refactor: Refactorización de código

test: Agregar o modificar tests

# 🧪 Guía de Comandos para Testing

## Comandos Básicos de Testing

### Ejecución Básica de Tests
```bash
# Ejecutar TODOS los tests en la carpeta tests/
pytest

# Ejecutar tests con detalles verbosos (-v = verbose)
pytest -v

# Ejecutar tests específicos de un archivo
pytest tests/test_fundamentos.py -v
pytest tests/test_ejercicios.py -v

# Ejecutar tests manualmente (sin pytest)
python tests/test_fundamentos.py
python tests/test_ejercicios.py

# Ejecutar tests y mostrar output de los tests que pasan
pytest -v -s

# Comando rápido para verificar que todo funciona
pytest -q

# Ejecutar tests usando el módulo de pytest
python -m pytest tests/






