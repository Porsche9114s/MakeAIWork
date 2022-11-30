from shape import Shape, math

class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self. height = height
  
    def area(self):
        return round(self.width * self.height)
