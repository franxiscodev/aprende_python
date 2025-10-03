#!/usr/bin/env python3
"""
🧪 TESTS: Ejercicios prácticos para testing

Más ejemplos simples de tests para practicar.
"""


def calcular_promedio(numeros: list) -> float:
    """Calcula el promedio de una lista de números"""
    if not numeros:
        return 0
    return sum(numeros) / len(numeros)


def encontrar_maximo(numeros: list) -> int:
    """Encuentra el número máximo en una lista"""
    if not numeros:
        return None
    return max(numeros)


def invertir_texto(texto: str) -> str:
    """Invierte un texto"""
    return texto[::-1]

# Tests


def test_calcular_promedio():
    """Test para calcular promedio"""
    assert calcular_promedio([1, 2, 3, 4, 5]) == 3.0
    assert calcular_promedio([10, 20, 30]) == 20.0
    assert calcular_promedio([]) == 0
    assert calcular_promedio([5]) == 5.0


def test_encontrar_maximo():
    """Test para encontrar máximo"""
    assert encontrar_maximo([1, 5, 3, 9, 2]) == 9
    assert encontrar_maximo([-1, -5, -3]) == -1
    assert encontrar_maximo([42]) == 42
    assert encontrar_maximo([]) is None


def test_invertir_texto():
    """Test para invertir texto"""
    assert invertir_texto("hola") == "aloh"
    assert invertir_texto("python") == "nohtyp"
    assert invertir_texto("") == ""
    assert invertir_texto("a") == "a"


def test_operaciones_lista():
    """Tests adicionales con listas"""
    # Ordenamiento
    numeros = [3, 1, 4, 1, 5, 9, 2]
    numeros.sort()
    assert numeros == [1, 1, 2, 3, 4, 5, 9]

    # Filtrado
    mayores = [x for x in numeros if x > 3]
    assert mayores == [4, 5, 9]

    # Mapeo
    dobles = [x * 2 for x in numeros]
    assert dobles == [2, 2, 4, 6, 8, 10, 18]
