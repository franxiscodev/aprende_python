#!/usr/bin/env python3
"""
🧪 TESTS: Pruebas para módulos de fundamentos usando pytest

Tests unitarios simples y prácticos para verificar el funcionamiento.
"""
import sys
import os

# Agregar el directorio raíz al path para importar módulos
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Funciones de ejemplo para testing (simulamos las que estarían en otros módulos)


def suma(a: int, b: int) -> int:
    """Función simple de suma para testing"""
    return a + b


def es_par(numero: int) -> bool:
    """Verifica si un número es par"""
    return numero % 2 == 0


def contar_vocales(texto: str) -> int:
    """Cuenta las vocales en un texto"""
    vocales = "aeiouAEIOU"
    return sum(1 for char in texto if char in vocales)


def filtrar_palabras_largas(palabras: list, longitud_minima: int = 5) -> list:
    """Filtra palabras más largas que longitud_minima"""
    return [palabra for palabra in palabras if len(palabra) > longitud_minima]

# Tests usando pytest


def test_suma_basica():
    """Test básico de suma"""
    assert suma(2, 3) == 5
    assert suma(-1, 1) == 0
    assert suma(0, 0) == 0


def test_suma_negativos():
    """Test de suma con números negativos"""
    assert suma(-5, -3) == -8
    assert suma(-10, 5) == -5


def test_es_par():
    """Test para función es_par"""
    assert es_par(2) == True
    assert es_par(3) == False
    assert es_par(0) == True
    assert es_par(-4) == True


def test_contar_vocales():
    """Test para contar vocales"""
    assert contar_vocales("hello") == 2
    assert contar_vocales("PYTHON") == 1
    assert contar_vocales("aeiou") == 5
    assert contar_vocales("xyz") == 0
    assert contar_vocales("") == 0


def test_filtrar_palabras_largas():
    """Test para filtrar palabras largas"""
    palabras = ["hola", "python", "si", "programacion", "no"]
    resultado = filtrar_palabras_largas(palabras, 4)
    assert resultado == ["python", "programacion"]

    resultado_corto = filtrar_palabras_largas(palabras, 2)
    assert resultado_corto == ["hola", "python", "programacion"]


def test_filtrar_palabras_vacio():
    """Test con lista vacía"""
    assert filtrar_palabras_largas([]) == []


def test_tipos_datos():
    """Tests con diferentes tipos de datos"""
    # Listas
    numeros = [1, 2, 3]
    assert len(numeros) == 3
    assert numeros[0] == 1

    # Tuplas
    coordenadas = (4, 5)
    assert coordenadas[1] == 5

    # Diccionarios
    persona = {"nombre": "Ana", "edad": 25}
    assert persona["nombre"] == "Ana"
    assert "edad" in persona


class TestClaseEjemplo:
    """Ejemplo de tests en una clase"""

    def test_multiplicacion(self):
        """Test de multiplicación simple"""
        assert 3 * 4 == 12
        assert 5 * 0 == 0

    def test_division(self):
        """Test de división"""
        assert 10 / 2 == 5
        assert 8 / 4 == 2


def test_list_comprehension():
    """Test para list comprehensions"""
    # Cuadrados
    cuadrados = [x**2 for x in range(1, 6)]
    assert cuadrados == [1, 4, 9, 16, 25]

    # Filtrado
    pares = [x for x in range(10) if x % 2 == 0]
    assert pares == [0, 2, 4, 6, 8]

    # Transformación de strings
    palabras = ["hi", "hello", "hey"]
    mayusculas = [p.upper() for p in palabras]
    assert mayusculas == ["HI", "HELLO", "HEY"]


def test_diccionario_comprehension():
    """Test para dictionary comprehensions"""
    cuadrados_dict = {x: x**2 for x in range(1, 4)}
    assert cuadrados_dict == {1: 1, 2: 4, 3: 9}

    # Con condición
    pares_dict = {x: x*2 for x in range(5) if x % 2 == 0}
    assert pares_dict == {0: 0, 2: 4, 4: 8}


def main():
    """Función principal para ejecutar tests manualmente"""
    print("🧪 EJECUTANDO TESTS BÁSICOS")
    print("=" * 40)

    # Ejecutar algunos tests manualmente para demostración
    try:
        # Test suma
        assert suma(2, 3) == 5, "Error en test_suma_basica"
        print("✅ test_suma_basica - PASÓ")

        # Test es_par
        assert es_par(4) == True, "Error en test_es_par"
        print("✅ test_es_par - PASÓ")

        # Test contar_vocales
        assert contar_vocales("hello") == 2, "Error en test_contar_vocales"
        print("✅ test_contar_vocales - PASÓ")

        print("\n🎯 Todos los tests manuales pasaron correctamente!")
        print("💡 Ejecuta 'pytest tests/test_fundamentos.py' para más detalles")

    except AssertionError as e:
        print(f"❌ Test falló: {e}")


if __name__ == "__main__":
    main()
