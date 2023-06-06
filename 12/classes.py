

class Shape:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self._color = color

    def area(self):
        return 42

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    # On ne fait pas ça en python :
    def getColor(self):
        return self._color

    # On fait ça en python :
    @property
    def color(self):
        return self._color


class Circle(Shape):  # Circle hérite de Shape
    def __init__(self, radius, x, y, color):
        # Appel du constructeur de Shape (parent) avec  le mot clé super()
        super().__init__(x, y, color)
        self._radius = radius

    def _compute_area(self):
        self.area = 3.14 * self.radius**2

    # Getter de radius
    @property
    def radius(self):
        return self._radius

    # Setter de radius
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value
        self._compute_area()
