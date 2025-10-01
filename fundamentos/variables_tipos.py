#!/usr/bin/env python3
"""
🔰 FUNDAMENTOS: Variables y Tipos de Datos

Este módulo cubre los conceptos básicos de variables y tipos en Python.
"""
import sys
from typing import Any


def demostrar_variables_basicas():
    """Demuestra variables básicas y tipos de datos"""
    print("1. 📝 VARIABLES BÁSICAS")
    print("-" * 40)

    # Enteros
    edad = 25
    cantidad_productos = 100
    print(f"Enteros: edad={edad}, cantidad={cantidad_productos}")

    # Flotantes
    precio = 19.99
    pi = 3.14159
    print(f"Flotantes: precio=${precio}, π={pi}")

    # Strings
    nombre = "Ana García"
    mensaje = 'Hola Mundo'
    print(f"Strings: nombre='{nombre}', mensaje='{mensaje}'")

    # Booleanos
    es_mayor = True
    tiene_descuento = False
    print(f"Booleanos: es_mayor={es_mayor}, tiene_descuento={tiene_descuento}")


def demostrar_tipado_dinamico():
    """Muestra el tipado dinámico de Python"""
    print("\n2. 🔄 TIPADO DINÁMICO")
    print("-" * 40)

    # Una variable puede cambiar de tipo
    variable_flexible = 10
    print(
        f"Valor inicial: {variable_flexible} (tipo: {type(variable_flexible)})")

    variable_flexible = "Ahora soy un string"
    print(
        f"Valor cambiado: {variable_flexible} (tipo: {type(variable_flexible)})")

    variable_flexible = 3.14
    print(
        f"Valor final: {variable_flexible} (tipo: {type(variable_flexible)})")


def demostrar_operaciones_comunes():
    """Demuestra operaciones comunes con diferentes tipos"""
    print("\n3. 🧮 OPERACIONES COMUNES")
    print("-" * 40)

    # Operaciones con números
    a, b = 15, 4
    print(f"Operaciones con {a} y {b}:")
    print(f"  Suma: {a} + {b} = {a + b}")
    print(f"  Resta: {a} - {b} = {a - b}")
    print(f"  Multiplicación: {a} * {b} = {a * b}")
    print(f"  División: {a} / {b} = {a / b}")
    print(f"  División entera: {a} // {b} = {a // b}")
    print(f"  Módulo: {a} % {b} = {a % b}")
    print(f"  Potencia: {a} ** {b} = {a ** b}")

    # Operaciones con strings
    nombre = "Python"
    version = "3.11"
    print(f"\nOperaciones con strings:")
    print(
        f"  Concatenación: '{nombre}' + ' ' + '{version}' = '{nombre + ' ' + version}'")
    print(f"  Repetición: '{nombre}' * 3 = '{nombre * 3}'")
    print(f"  Mayúsculas: '{nombre}'.upper() = '{nombre.upper()}'")
    print(f"  Longitud: len('{nombre}') = {len(nombre)}")


def demostrar_conversion_tipos():
    """Muestra cómo convertir entre tipos de datos"""
    print("\n4. 🔄 CONVERSIÓN DE TIPOS")
    print("-" * 40)

    # Conversiones comunes
    numero_str = "123"
    numero_int = int(numero_str)
    numero_float = float(numero_str)

    print(f"String a entero: int('{numero_str}') = {numero_int}")
    print(f"String a float: float('{numero_str}') = {numero_float}")

    # Float a int (truncamiento)
    precio = 19.99
    precio_entero = int(precio)
    print(f"Float a entero: int({precio}) = {precio_entero}")

    # Número a string
    edad = 25
    edad_str = str(edad)
    print(f"Entero a string: str({edad}) = '{edad_str}'")

    # Booleanos
    print(f"Entero a booleano: bool(0) = {bool(0)}, bool(1) = {bool(1)}")
    print(
        f"String a booleano: bool('') = {bool('')}, bool('Hola') = {bool('Hola')}")


def ejercicios_practicos():
    """Ejercicios para practicar con variables y tipos"""
    print("\n5. 💪 EJERCICIOS PRÁCTICOS")
    print("-" * 40)

    print("Ejercicio 1: Calculadora básica")
    num1, num2 = 8, 3
    print(f"  Con {num1} y {num2}:")
    print(f"  Suma: {num1 + num2}")
    print(f"  Multiplicación: {num1 * num2}")

    print("\nEjercicio 2: Manipulación de strings")
    lenguaje = "python"
    print(f"  Original: '{lenguaje}'")
    print(f"  Mayúsculas: '{lenguaje.upper()}'")
    print(f"  Capitalizado: '{lenguaje.capitalize()}'")
    print(f"  Longitud: {len(lenguaje)}")

    print("\nEjercicio 3: Conversiones")
    temperatura = "36.5"
    temp_float = float(temperatura)
    print(f"  Temperatura string: '{temperatura}'")
    print(f"  Temperatura float: {temp_float}")


def main():
    """Función principal del módulo de variables y tipos"""
    print("🎓 VARIABLES Y TIPOS DE DATOS EN PYTHON")
    print("=" * 60)

    demostrar_variables_basicas()
    demostrar_tipado_dinamico()
    demostrar_operaciones_comunes()
    demostrar_conversion_tipos()
    ejercicios_practicos()

    print("\n" + "✅ MÓDULO COMPLETADO".center(60, "="))
    print("¡Has aprendido los fundamentos de variables y tipos en Python!")


if __name__ == "__main__":
    main()
