#!/usr/bin/env python3
"""
🔰 FUNDAMENTOS: Funciones

Este módulo cubre la creación y uso de funciones en Python.
"""
from typing import List, Dict, Union, Optional


def funciones_simples():
    """Demuestra funciones simples sin parámetros"""
    print("1. 📝 FUNCIONES SIMPLES")
    print("-" * 40)

    def saludar():
        """Función que simplemente saluda"""
        return "¡Hola desde una función!"

    def mostrar_fecha():
        """Función que muestra información"""
        from datetime import datetime
        return f"Fecha actual: {datetime.now().strftime('%Y-%m-%d')}"

    print(saludar())
    print(mostrar_fecha())


def funciones_con_parametros():
    """Demuestra funciones con parámetros"""
    print("\n2. 🎯 FUNCIONES CON PARÁMETROS")
    print("-" * 40)

    def calcular_area_rectangulo(largo: float, ancho: float) -> float:
        """Calcula el área de un rectángulo"""
        return largo * ancho

    def personalizar_saludo(nombre: str, lenguaje: str = "Python") -> str:
        """Saluda personalizadamente"""
        return f"¡Hola {nombre}! Bienvenido a {lenguaje}"

    area = calcular_area_rectangulo(5, 3)
    print(f"Área de rectángulo 5x3: {area}")

    saludo1 = personalizar_saludo("Ana")
    saludo2 = personalizar_saludo("Carlos", "JavaScript")
    print(saludo1)
    print(saludo2)


def funciones_con_valores_por_defecto():
    """Demuestra parámetros con valores por defecto"""
    print("\n3. ⚙️ PARÁMETROS POR DEFECTO")
    print("-" * 40)

    def crear_usuario(nombre: str, edad: int, pais: str = "Desconocido", activo: bool = True) -> Dict:
        """Crea un usuario con parámetros opcionales"""
        return {
            "nombre": nombre,
            "edad": edad,
            "pais": pais,
            "activo": activo
        }

    usuario1 = crear_usuario("María", 25)
    usuario2 = crear_usuario("Juan", 30, "España")
    usuario3 = crear_usuario("Luis", 35, "México", False)

    print("Usuario 1:", usuario1)
    print("Usuario 2:", usuario2)
    print("Usuario 3:", usuario3)


def funciones_con_retorno_multiple():
    """Demuestra retorno de múltiples valores"""
    print("\n4. 🔄 RETORNO MÚLTIPLE")
    print("-" * 40)

    def operaciones_matematicas(a: float, b: float) -> tuple:
        """Realiza múltiples operaciones y retorna resultados"""
        suma = a + b
        resta = a - b
        multiplicacion = a * b
        division = a / b if b != 0 else "Indefinido"

        return suma, resta, multiplicacion, division

    def analizar_lista(numeros: List[int]) -> tuple:
        """Analiza una lista y retorna estadísticas"""
        if not numeros:
            return 0, 0, 0

        return min(numeros), max(numeros), sum(numeros) / len(numeros)

    # Ejemplo 1
    a, b = 10, 3
    resultados = operaciones_matematicas(a, b)
    print(f"Operaciones con {a} y {b}:")
    print(f"  Suma: {resultados[0]}")
    print(f"  Resta: {resultados[1]}")
    print(f"  Multiplicación: {resultados[2]}")
    print(f"  División: {resultados[3]}")

    # Ejemplo 2
    lista = [5, 2, 8, 1, 9, 3]
    minimo, maximo, promedio = analizar_lista(lista)
    print(f"\nAnálisis de lista {lista}:")
    print(f"  Mínimo: {minimo}")
    print(f"  Máximo: {maximo}")
    print(f"  Promedio: {promedio:.2f}")


def funciones_recursivas():
    """Demuestra funciones recursivas"""
    print("\n5. 🔁 FUNCIONES RECURSIVAS")
    print("-" * 40)

    def factorial(n: int) -> int:
        """Calcula factorial de forma recursiva"""
        if n == 0 or n == 1:
            return 1
        return n * factorial(n - 1)

    def fibonacci(n: int) -> int:
        """Calcula el n-ésimo número de Fibonacci"""
        if n <= 1:
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)

    print("Factoriales:")
    for i in range(1, 6):
        print(f"  {i}! = {factorial(i)}")

    print("\nSecuencia de Fibonacci:")
    for i in range(10):
        print(f"  F({i}) = {fibonacci(i)}")


def funciones_como_ciudadanos():
    """Demuestra que las funciones son ciudadanos de primera clase"""
    print("\n6. 🏆 FUNCIONES COMO CIUDADANOS DE PRIMERA CLASE")
    print("-" * 40)

    # Función como variable
    def duplicar(x): return x * 2
    print(f"Duplicar 5: {duplicar(5)}")

    # Función como parámetro
    def aplicar_funcion(func, valor):
        """Aplica una función a un valor"""
        return func(valor)

    resultado = aplicar_funcion(duplicar, 10)
    print(f"Aplicar duplicar a 10: {resultado}")

    # Función que retorna función
    def crear_multiplicador(factor):
        """Crea una función multiplicadora"""
        def multiplicar(x):
            return x * factor
        return multiplicar

    triplicar = crear_multiplicador(3)
    print(f"Triplicar 7: {triplicar(7)}")


def ejercicios_practicos():
    """Ejercicios para practicar con funciones"""
    print("\n7. 💪 EJERCICIOS PRÁCTICOS")
    print("-" * 40)

    # Ejercicio 1: Contador de palabras
    def contar_palabras(texto: str) -> Dict[str, int]:
        """Cuenta la frecuencia de palabras en un texto"""
        palabras = texto.lower().split()
        frecuencia = {}

        for palabra in palabras:
            frecuencia[palabra] = frecuencia.get(palabra, 0) + 1

        return frecuencia

    texto = "python es genial y python es poderoso"
    resultado = contar_palabras(texto)
    print(f"Frecuencia de palabras: {resultado}")

    # Ejercicio 2: Calculadora simple
    def calculadora(a: float, b: float, operacion: str) -> float:
        """Calculadora simple con diferentes operaciones"""
        operaciones = {
            'suma': a + b,
            'resta': a - b,
            'multiplicacion': a * b,
            'division': a / b if b != 0 else "Error"
        }
        return operaciones.get(operacion, "Operación no válida")

    print(f"\nCalculadora:")
    print(f"  5 + 3 = {calculadora(5, 3, 'suma')}")
    print(f"  5 - 3 = {calculadora(5, 3, 'resta')}")
    print(f"  5 * 3 = {calculadora(5, 3, 'multiplicacion')}")


def main():
    """Función principal del módulo de funciones"""
    print("🎓 FUNCIONES EN PYTHON")
    print("=" * 60)

    funciones_simples()
    funciones_con_parametros()
    funciones_con_valores_por_defecto()
    funciones_con_retorno_multiple()
    funciones_recursivas()
    funciones_como_ciudadanos()
    ejercicios_practicos()

    print("\n" + "✅ MÓDULO COMPLETADO".center(60, "="))
    print("¡Has dominado el arte de las funciones en Python!")


if __name__ == "__main__":
    main()
