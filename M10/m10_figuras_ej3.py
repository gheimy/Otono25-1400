# --------------------------------------------------------------------------
#          DEMOSTRACIÓN DE POLIMORFISMO CON FORMAS GEOMÉTRICAS
# --------------------------------------------------------------------------

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def dibujar(self):
        print(f"Dibujando un círculo de radio {self.radio}.")


class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def dibujar(self):
        print(f"Dibujando un rectángulo de {self.ancho}x{self.alto}.")


class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def dibujar(self):
        print(f"Dibujando un triángulo de base {self.base} y altura {self.altura}.")


# --- Bloque para probar tus clases ---
if __name__ == "__main__":
    formas = [
        Circulo(10),
        Rectangulo(20, 30),
        Triangulo(15, 25)
    ]

    print("--- Dibujando todas las formas ---")
    for forma in formas:
        forma.dibujar()
