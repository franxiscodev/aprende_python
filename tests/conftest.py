"""
Configuración global para pytest
"""
import sys
import os

# Agregar el directorio raíz al path de Python
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))
