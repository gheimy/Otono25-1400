# line_midpoint.py
# TODO #2: midpoint() que devuelve el punto medio de un segmento

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def midpoint(self):
        """
        Devuelve el punto medio entre p1 y p2.
        """
        mid_x = (self.p1.x + self.p2.x) / 2
        mid_y = (self.p1.y + self.p2.y) / 2
        return Point(mid_x, mid_y)

# Ejemplo de prueba
if __name__ == "__main__":
    p1 = Point(2, 4)
    p2 = Point(6, 8)

    l = Line(p1, p2)
    print("Midpoint:", l.midpoint())  # debe ser Point(4, 6)
