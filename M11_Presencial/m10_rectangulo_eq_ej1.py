# --------------------------------------------------------------------------
#          CLASE RECTANGULO CON COMPARACIÓN DE EQUIVALENCIA
# --------------------------------------------------------------------------
# Descripción:
# El objetivo es entender la diferencia entre identidad (`is`) y
# equivalencia (`==`). Modificaremos la clase `Rectangulo` para que
# dos objetos se consideren "iguales" si tienen las mismas dimensiones,
# aunque no sean el mismo objeto en memoria.
#
# Instrucciones:
# 1. Verificar si `otro` es una instancia de Rectangulo.
# 2. Comparar ancho y alto entre self y otro.
# --------------------------------------------------------------------------

class Rectangulo:
    """Una clase para representar un rectángulo."""

    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
    def __eq__(self, otro):
        """
        Comprueba si este rectángulo es equivalente a otro.
        """
        # Paso 1: verificar si `otro` es instancia de Rectangulo
        if not isinstance(otro, Rectangulo):
            return False

        # Paso 2: comparar dimensiones
        return self.ancho == otro.ancho and self.alto == otro.alto



# --- Bloque de pruebas ---
if __name__ == "__main__":
    r1 = Rectangulo(10, 20)
    r2 = Rectangulo(10, 20)  # Otro objeto con mismos valores
    r3 = r1                  # Misma referencia en memoria

    print("--- Comparando r1 y r2 ---")
    print(f"r1 == r2 (Equivalencia): {r1 == r2}")
    print(f"r1 is r2 (Identidad):    {r1 is r2}")

    print("\n--- Comparando r1 y r3 ---")
    print(f"r1 == r3 (Equivalencia): {r1 == r3}")
    print(f"r1 is r3 (Identidad):    {r1 is r3}")
