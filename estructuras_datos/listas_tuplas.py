#!/usr/bin/env python3
"""
🏗️ ESTRUCTURAS DE DATOS: Listas y Tuplas

Este módulo cubre el trabajo con listas y tuplas en Python.
"""
from typing import List, Tuple, Any


def demostrar_listas_basicas():
    """Demuestra operaciones básicas con listas"""
    print("1. 📝 LISTAS - OPERACIONES BÁSICAS")
    print("-" * 40)

    # Creación de listas
    numeros = [1, 2, 3, 4, 5]
    frutas = ["manzana", "banana", "naranja"]
    mixta = [1, "hola", 3.14, True]

    print(f"Lista de números: {numeros}")
    print(f"Lista de frutas: {frutas}")
    print(f"Lista mixta: {mixta}")

    # Acceso a elementos
    print(f"\nAcceso a elementos:")
    print(f"  Primer elemento: {numeros[0]}")
    print(f"  Último elemento: {numeros[-1]}")
    print(f"  Rango: {numeros[1:4]}")

    # Modificación
    numeros[0] = 100
    print(f"\nDespués de modificar: {numeros}")


def demostrar_metodos_listas():
    """Demuestra métodos útiles de listas"""
    print("\n2. 🔧 LISTAS - MÉTODOS ÚTILES")
    print("-" * 40)

    lista = [3, 1, 4, 1, 5, 9, 2]
    print(f"Lista original: {lista}")

    # Agregar elementos
    lista.append(6)
    print(f"Después de append(6): {lista}")

    lista.insert(2, 99)
    print(f"Después de insert(2, 99): {lista}")

    # Remover elementos
    lista.remove(1)
    print(f"Después de remove(1): {lista}")

    elemento = lista.pop()
    print(f"Elemento removido con pop(): {elemento}")
    print(f"Lista después del pop: {lista}")

    # Ordenar
    lista.sort()
    print(f"Lista ordenada: {lista}")

    lista.reverse()
    print(f"Lista invertida: {lista}")


def demostrar_comprehensions():
    """Demuestra list comprehensions"""
    print("\n3. 🎯 LIST COMPREHENSIONS")
    print("-" * 40)

    # List comprehension básico
    cuadrados = [x**2 for x in range(1, 6)]
    print(f"Cuadrados del 1-5: {cuadrados}")

    # Con condición
    pares = [x for x in range(10) if x % 2 == 0]
    print(f"Números pares del 0-9: {pares}")

    # Transformación de datos
    palabras = ["python", "es", "genial"]
    mayusculas = [p.upper() for p in palabras]
    print(f"Palabras en mayúsculas: {mayusculas}")

    # List comprehension anidado
    matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    aplanada = [num for fila in matriz for num in fila]
    print(f"Matriz aplanada: {aplanada}")


def demostrar_tuplas():
    """Demuestra el uso de tuplas"""
    print("\n4. 📦 TUPLAS - INMUTABLES")
    print("-" * 40)

    # Creación de tuplas
    coordenadas = (4, 5)
    colores = ("rojo", "verde", "azul")
    tupla_un_elemento = (42,)  # ¡Importante la coma!

    print(f"Coordenadas: {coordenadas}")
    print(f"Colores: {colores}")
    print(f"Tupla un elemento: {tupla_un_elemento}")

    # Acceso a elementos (igual que listas)
    print(f"Primer color: {colores[0]}")
    print(f"Último color: {colores[-1]}")

    # Desempaquetado de tuplas
    x, y = coordenadas
    print(f"Desempaquetado: x={x}, y={y}")

    # Las tuplas son inmutables
    try:
        coordenadas[0] = 10
    except TypeError as e:
        print(f"Error al modificar tupla: {e}")


def ejercicios_practicos():
    """Ejercicios para practicar con listas y tuplas"""
    print("\n5. 💪 EJERCICIOS PRÁCTICOS")
    print("-" * 40)

    print("Ejercicio 1: Filtrado y transformación")
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    resultado = [x**2 for x in numeros if x % 2 == 0]
    print(f"Cuadrados de números pares: {resultado}")

    print("\nEjercicio 2: Estadísticas de lista")
    datos = [23, 45, 12, 67, 89, 34, 56]
    print(f"Datos: {datos}")
    print(f"  Máximo: {max(datos)}")
    print(f"  Mínimo: {min(datos)}")
    print(f"  Suma: {sum(datos)}")
    print(f"  Promedio: {sum(datos)/len(datos):.2f}")

    print("\nEjercicio 3: Manipulación de strings")
    texto = "python es un lenguaje de programación"
    palabras = texto.split()
    palabras_largas = [p for p in palabras if len(p) > 4]
    print(f"Palabras largas: {palabras_largas}")


def proyecto_integrador():
    """Proyecto integrador: Gestor de tareas simple"""
    print("\n6. 🎓 PROYECTO INTEGRADOR: GESTOR DE TAREAS")
    print("-" * 40)

    # Sistema simple de gestión de tareas
    tareas = []

    def agregar_tarea(descripcion, prioridad="media"):
        tareas.append({
            "descripcion": descripcion,
            "prioridad": prioridad,
            "completada": False
        })

    def mostrar_tareas():
        if not tareas:
            print("  No hay tareas pendientes")
            return

        for i, tarea in enumerate(tareas, 1):
            estado = "✓" if tarea["completada"] else " "
            print(
                f"  {i}. [{estado}] {tarea['descripcion']} ({tarea['prioridad']})")

    def completar_tarea(indice):
        if 0 <= indice - 1 < len(tareas):
            tareas[indice - 1]["completada"] = True
            print(f"  Tarea {indice} marcada como completada")
        else:
            print("  Índice inválido")

    # Demo del gestor de tareas
    print("Gestor de Tareas Simple:")
    agregar_tarea("Aprender Python", "alta")
    agregar_tarea("Practicar ejercicios", "media")
    agregar_tarea("Leer documentación", "baja")

    print("\nTareas iniciales:")
    mostrar_tareas()

    completar_tarea(1)
    print("\nDespués de completar primera tarea:")
    mostrar_tareas()


def main():
    """Función principal del módulo de listas y tuplas"""
    print("🎓 LISTAS Y TUPLAS EN PYTHON")
    print("=" * 60)

    demostrar_listas_basicas()
    demostrar_metodos_listas()
    demostrar_comprehensions()
    demostrar_tuplas()
    ejercicios_practicos()
    proyecto_integrador()

    print("\n" + "✅ MÓDULO COMPLETADO".center(60, "="))
    print("¡Has dominado las listas y tuplas en Python!")


if __name__ == "__main__":
    main()
