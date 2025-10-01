#!/usr/bin/env python3
"""
👋 HELLO PYTHON - Edición Vitaminada

Un Hello World ampliado que muestra varias características de Python.
"""
import datetime
import random
import sys
from typing import Dict, List


def mostrar_banner() -> None:
    """Muestra un banner decorativo"""
    banner = """
    ╔══════════════════════════════════════════╗
    ║           🐍 HELLO PYTHON 🐍             ║
    ║         Edición Super Vitaminada         ║
    ╚══════════════════════════════════════════╝
    """
    print(banner)


def obtener_info_usuario() -> Dict[str, str]:
    """Recolecta información del usuario de forma interactiva"""
    print("\n👋 ¡Hola! Vamos a conocernos mejor...")

    nombre = input("¿Cuál es tu nombre? ").strip() or "Aprendiz Python"
    lenguaje = input("¿Qué lenguaje te gusta? ").strip() or "Python"
    experiencia = input(
        "¿Nivel de experiencia (principiante/intermedio/avanzado)? ").strip() or "principiante"

    return {
        "nombre": nombre,
        "lenguaje": lenguaje,
        "experiencia": experiencia,
        "fecha": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "python_version": sys.version.split()[0],
        "sistema": sys.platform
    }


def generar_saludo_personalizado(datos: Dict[str, str]) -> str:
    """Genera un saludo personalizado basado en los datos"""
    saludos = ["¡Hola", "Bienvenido/a", "Un gusto", "Saludos", "¡Qué tal"]
    adjetivos = ["increíble", "fantástico",
                 "asombroso", "genial", "maravilloso"]

    saludo = random.choice(saludos)
    adjetivo = random.choice(adjetivos)

    mensaje = f"""
    {saludo} {datos['nombre']}! 🎉

    📊 Información de tu sesión:
    • Fecha y hora: {datos['fecha']}
    • Versión Python: {datos['python_version']}
    • Sistema: {datos['sistema']}
    • Lenguaje favorito: {datos['lenguaje']}
    • Nivel: {datos['experiencia']}

    🚀 ¡Estás a punto de comenzar un viaje {adjetivo} 
       aprendiendo Python!

    💡 Tip del día: 
    {obtener_tip_aleatorio()}
    """
    return mensaje


def obtener_tip_aleatorio() -> str:
    """Retorna un tip aleatorio sobre Python"""
    tips = [
        "En Python, todo es un objeto 🎯",
        "Usa list comprehensions para código más limpio ✨",
        "Los decoradores son tus amigos para extender funcionalidades 🎁",
        "Aprende a usar 'virtualenv' para manejar dependencias 📦",
        "La documentación con docstrings es esencial 📝",
        "Practica todos los días, incluso 15 minutos hacen la diferencia ⏱️",
        "Los f-strings son la mejor forma de formatear strings 🎪",
        "Aprende a usar type hints para código más mantenible 🎯"
    ]
    return random.choice(tips)


def demostrar_caracteristicas_python() -> None:
    """Demuestra características interesantes de Python"""
    print("\n" + "🔍 DEMOSTRACIÓN RÁPIDA DE PYTHON".center(50, "="))

    # List comprehension
    numeros = [x for x in range(1, 6)]
    cuadrados = [x**2 for x in numeros]
    print(f"📊 List comprehension: {numeros} → {cuadrados}")

    # Dictionary comprehension
    cubos = {f"{x}³": x**3 for x in numeros}
    print(f"📚 Dict comprehension: {cubos}")

    # F-strings avanzados
    producto = "Python"
    version = 3.11
    print(
        f"🎪 F-strings: {producto} {version} es {['lento', 'rápido'][version > 3.6]} 💨")

    # Multiple assignment
    a, b, c = 1, 2, 3
    print(f"🔄 Multiple assignment: a={a}, b={b}, c={c}")


def crear_archivo_bienvenida(nombre: str) -> None:
    """Crea un archivo de bienvenida personalizado"""
    nombre_archivo = f"bienvenida_{nombre.lower().replace(' ', '_')}.txt"
    contenido = f"""
    ¡Bienvenido/a {nombre}!
    
    Fecha de creación: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    
    Mensaje:
    ¡Felicidades por dar tus primeros pasos en Python!
    Este archivo fue generado automáticamente por tu programa.
    
    Recuerda: La práctica constante es la clave del éxito.
    
    ¡Sigue programando! 🐍
    """

    try:
        with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
            archivo.write(contenido)
        print(f"📁 Archivo '{nombre_archivo}' creado exitosamente!")
    except Exception as e:
        print(f"❌ Error creando archivo: {e}")


def main():
    """Función principal del Hello World Vitaminado"""
    try:
        mostrar_banner()

        # Obtener información del usuario
        datos_usuario = obtener_info_usuario()

        # Mostrar mensaje personalizado
        mensaje = generar_saludo_personalizado(datos_usuario)
        print(mensaje)

        # Demostrar características de Python
        demostrar_caracteristicas_python()

        # Crear archivo de bienvenida
        crear_archivo_bienvenida(datos_usuario["nombre"])

        # Mensaje final
        print("\n" + "🎊 ¡FELICIDADES! ".center(50, "="))
        print("Has ejecutado tu primer programa Python 'vitaminado'")
        print("Revisa el archivo de bienvenida que se creó")
        print("=" * 50)

    except KeyboardInterrupt:
        print("\n\n⏹️  Ejecución interrumpida. ¡Hasta pronto!")
    except Exception as e:
        print(f"\n❌ Ocurrió un error: {e}")


if __name__ == "__main__":
    main()
