#!/usr/bin/env python3
"""
🐍 APRENDE PYTHON - Punto de Entrada Principal

Un sistema modular para aprender Python de manera organizada.
Cada módulo contiene ejemplos y ejercicios sobre temas específicos.
"""
import importlib
import sys
from pathlib import Path


def mostrar_banner():
    """Muestra el banner de bienvenida"""
    banner = """
    ╔══════════════════════════════════════════════════╗
    ║               🐍 APRENDE PYTHON 🐍              ║
    ║          Laboratorio de Aprendizaje              ║
    ║                                                  ║
    ║     ¡Bienvenido a tu viaje de aprendizaje!       ║
    ╚══════════════════════════════════════════════════╝
    """
    print(banner)


def mostrar_modulos_disponibles():
    """Muestra los módulos de aprendizaje disponibles"""
    modulos = {
        "1": {"nombre": "Variables y Tipos", "modulo": "🔰 fundamentos", "archivo": "variables_tipos"},
        "2": {"nombre": "Estructuras de Control", "modulo": "🔰 fundamentos", "archivo": "estructuras_control"},
        "3": {"nombre": "Funciones", "modulo": "🔰 fundamentos", "archivo": "funciones"},
        "4": {"nombre": "Hello Python", "modulo": "👋 holapython", "archivo": "hello_world"},
        "5": {"nombre": "Listas y Tuplas", "modulo": "🏗️ *estructuras_datos", "archivo": "listas_tuplas"},
        "6": {"nombre": "Tests", "modulo": "🧪 tests", "archivo": "test_fundamentos"},
        "0": {"nombre": "Salir", "modulo": "🚪 Exit", "archivo": ""}
    }

    print("\n📚 MÓDULOS DE APRENDIZAJE DISPONIBLES:")
    print("=" * 50)
    for key, info in modulos.items():
        print(
            f"{key}. {info['modulo']}: {info['nombre']} - {info['archivo']}.py")
    print("0. 🚪 Salir")
    print("=" * 50)

    return modulos


def ejecutar_modulo(modulo, archivo):
    """Ejecuta un módulo específico de aprendizaje"""
    try:
        # Importar el módulo dinámicamente
        ruta_modulo = f"{modulo}.{archivo}"
        module = importlib.import_module(ruta_modulo)

        # Ejecutar la función main si existe
        if hasattr(module, 'main'):
            print(f"\n🎯 Ejecutando: {ruta_modulo}")
            print("=" * 40)
            module.main()
            return True
        else:
            print(f"⚠️  El módulo {ruta_modulo} no tiene función 'main'")
            return False

    except ImportError as e:
        print(f"❌ Error: No se pudo cargar el módulo {ruta_modulo}")
        print(f"   Detalle: {e}")
        return False
    except Exception as e:
        print(f"💥 Error ejecutando el módulo: {e}")
        return False


def main():
    """Función principal del sistema de aprendizaje"""
    try:
        mostrar_banner()

        while True:
            modulos = mostrar_modulos_disponibles()
            opcion = input("\n🎮 Selecciona un módulo (0-7): ").strip()

            if opcion == "0":
                print("\n👋 ¡Hasta luego! Sigue practicando Python 🐍")
                break

            if opcion in modulos:
                info_modulo = modulos[opcion]
                exito = ejecutar_modulo(
                    info_modulo["modulo"], info_modulo["archivo"])

                if not exito:
                    print(
                        f"💡 Tip: El archivo {info_modulo['archivo']}.py no existe aún.")
                    print("   Puedes crearlo siguiendo la estructura del proyecto.")

                input("\n⏎ Presiona Enter para continuar...")
            else:
                print("❌ Opción inválida. Intenta nuevamente.")

    except KeyboardInterrupt:
        print("\n\n🛑 Ejecución interrumpida. ¡Hasta pronto!")
    except Exception as e:
        print(f"\n💥 Error inesperado: {e}")


if __name__ == "__main__":
    # Verificar Python version
    if sys.version_info < (3, 8):
        print("❌ Se requiere Python 3.8 o superior")
        sys.exit(1)

    main()
