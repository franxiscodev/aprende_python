#!/usr/bin/env python3
"""
🔰 FUNDAMENTOS: Estructuras de Control

Este módulo cubre if/else, bucles for/while y control de flujo.
"""
import random


def demostrar_condicionales():
    """Demuestra el uso de if, elif, else"""
    print("1. 🎯 CONDICIONALES (if/elif/else)")
    print("-" * 40)

    # Ejemplo básico
    edad = 20
    print(f"Edad: {edad}")
    if edad < 18:
        print("  Eres menor de edad")
    elif 18 <= edad < 65:
        print("  Eres adulto")
    else:
        print("  Eres adulto mayor")

    # Condicionales múltiples
    puntuacion = 85
    print(f"\nPuntuación: {puntuacion}")
    if puntuacion >= 90:
        print("  Calificación: A")
    elif puntuacion >= 80:
        print("  Calificación: B")
    elif puntuacion >= 70:
        print("  Calificación: C")
    else:
        print("  Calificación: D")


def demostrar_bucle_for():
    """Demuestra el uso del bucle for"""
    print("\n2. 🔄 BUCLE FOR")
    print("-" * 40)

    # Bucle sobre lista
    frutas = ["manzana", "banana", "naranja", "uva"]
    print("Frutas en la lista:")
    for fruta in frutas:
        print(f"  - {fruta}")

    # Bucle con enumerate
    print("\nFrutas con índice:")
    for indice, fruta in enumerate(frutas, 1):
        print(f"  {indice}. {fruta}")

    # Bucle sobre rango
    print("\nNúmeros del 1 al 5:")
    for i in range(1, 6):
        print(f"  Número: {i}")


def demostrar_bucle_while():
    """Demuestra el uso del bucle while"""
    print("\n3. ⏳ BUCLE WHILE")
    print("-" * 40)

    # Contador simple
    contador = 5
    print("Cuenta regresiva:")
    while contador > 0:
        print(f"  {contador}...")
        contador -= 1
    print("  ¡Despegue! 🚀")

    # While con condición compleja
    numero_secreto = random.randint(1, 10)
    intentos = 3
    print(f"\nAdivina el número (1-10). Tienes {intentos} intentos:")

    while intentos > 0:
        try:
            guess = int(input("  Tu intento: "))
            if guess == numero_secreto:
                print("  ¡Correcto! 🎉")
                break
            else:
                intentos -= 1
                print(f"  Incorrecto. Te quedan {intentos} intentos")
        except ValueError:
            print("  Por favor, ingresa un número válido")

    if intentos == 0:
        print(f"  El número era: {numero_secreto}")


def demostrar_control_flujo():
    """Demuestra break, continue y pass"""
    print("\n4. 🎮 CONTROL DE FLUJO (break/continue/pass)")
    print("-" * 40)

    # Break - salir del bucle
    print("Break (buscar el número 5):")
    for i in range(1, 11):
        if i == 5:
            print(f"  ¡Encontrado {i}! Saliendo del bucle...")
            break
        print(f"  Probando {i}...")

    # Continue - saltar iteración
    print("\nContinue (números pares del 1 al 10):")
    for i in range(1, 11):
        if i % 2 != 0:  # Si es impar
            continue
        print(f"  Número par: {i}")

    # Pass - placeholder
    print("\nPass (estructura por implementar):")
    temperatura = 25
    if temperatura > 30:
        pass  # Por implementar: lógica para calor extremo
    else:
        print("  Temperatura normal")


def ejercicios_practicos():
    """Ejercicios para practicar estructuras de control"""
    print("\n5. 💪 EJERCICIOS PRÁCTICOS")
    print("-" * 40)

    print("Ejercicio 1: Números divisibles por 3 o 5")
    for i in range(1, 16):
        if i % 3 == 0 or i % 5 == 0:
            print(f"  {i} es divisible por 3 o 5")

    print("\nEjercicio 2: Suma de números pares")
    suma_pares = 0
    for i in range(1, 11):
        if i % 2 == 0:
            suma_pares += i
    print(f"  Suma de números pares del 1 al 10: {suma_pares}")

    print("\nEjercicio 3: Contador de vocales")
    texto = "Python es asombroso"
    vocales = "aeiouAEIOU"
    contador_vocales = 0

    for letra in texto:
        if letra in vocales:
            contador_vocales += 1

    print(f"  Texto: '{texto}'")
    print(f"  Número de vocales: {contador_vocales}")


def main():
    """Función principal del módulo de estructuras de control"""
    print("🎓 ESTRUCTURAS DE CONTROL EN PYTHON")
    print("=" * 60)

    demostrar_condicionales()
    demostrar_bucle_for()
    demostrar_bucle_while()
    demostrar_control_flujo()
    ejercicios_practicos()

    print("\n" + "✅ MÓDULO COMPLETADO".center(60, "="))
    print("¡Has aprendido a controlar el flujo de tus programas!")


if __name__ == "__main__":
    main()
