# rectangle_midpoint.py
# TODO #3: midpoint() que encuentra el centro del rectángulo

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

class Rectangle:
    def __init__(self, lower_left, upper_right):
        """
        lower_left: punto inferior izquierdo
        upper_right: punto superior derecho
        """
        self.lower_left = lower_left
        self.upper_right = upper_right

    def midpoint(self):
        """
        Centro del rectángulo:
        (x1 + x2)/2 , (y1 + y2)/2
        """
        center_x = (self.lower_left.x + self.upper_right.x) / 2
        center_y = (self.lower_left.y + self.upper_right.y) / 2
        return Point(center_x, center_y)

# Ejemplo de prueba
if __name__ == "__main__":
    p1 = Point(0, 0)
    p2 = Point(10, 8)

    r = Rectangle(p1, p2)
    print("Midpoint del rectángulo:", r.midpoint())  # Point(5, 4)
