# line_eq.py
# TODO #1: Implementar __eq__ para Line

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __eq__(self, other):
        """
        Dos líneas son iguales si sus puntos son equivalentes sin importar el orden.
        """
        return ((self.p1 == other.p1 and self.p2 == other.p2) or
                (self.p1 == other.p2 and self.p2 == other.p1))

# Ejemplo de prueba:
if __name__ == "__main__":
    a = Point(0, 0)
    b = Point(3, 4)
    c = Point(3, 4)
    d = Point(0, 0)

    line1 = Line(a, b)
    line2 = Line(c, d)  # deben ser iguales aunque estén invertidos

    print("¿Line1 == Line2?", line1 == line2)
