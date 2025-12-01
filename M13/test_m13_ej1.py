# test_formatear_usuario.py
# Archivo de pruebas para la función formatear_nombre_usuario.

import pytest

try:
    from m13_limpiar_ej1 import formatear_nombre_usuario
except ImportError:
    pytest.fail(
        "No se pudo importar la función 'formatear_nombre_usuario' desde 'm13_limpiar_ej1.py'."
    )


def test_nombre_valido():
    assert formatear_nombre_usuario("usuario") == "usuario"


def test_limpia_espacios():
    assert formatear_nombre_usuario("  pepito  ") == "pepito"


def test_convierte_a_minusculas():
    assert formatear_nombre_usuario("MARIA") == "maria"


def test_limpia_y_convierte():
    assert formatear_nombre_usuario("  CARLOS  ") == "carlos"


def test_invalido_con_numeros():
    assert formatear_nombre_usuario(
        "usuario123") == "Error: el nombre de usuario solo puede contener letras."


def test_invalido_con_simbolos():
    assert formatear_nombre_usuario(
        "user-name") == "Error: el nombre de usuario solo puede contener letras."
    assert formatear_nombre_usuario(
        "test@test") == "Error: el nombre de usuario solo puede contener letras."


def test_cadena_vacia_despues_de_limpiar():
    assert formatear_nombre_usuario(
        "   ") == "Error: el nombre de usuario solo puede contener letras."


if __name__ == "__main__":
    if pytest.main([__file__]) == 0:
        print("✅ Pruebas pasadas para el ejercicio de variables.")
    else:
        print("❌ Error en el código")
        print("Este módulo no se puede ejecutar directamente. Usa pytest para correr las pruebas.")
