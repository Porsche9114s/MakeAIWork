from shape import Shape, math

class Circle(Shape):
    def __init__(self, width):
        self.width = width
        super().__init__(width, width)
    
    def perimeter(self):
        return round(0.5 * self.width * self.Height * math.pi)

    def area(self):
        return round(math.pi *((self.width / 2) **2))
