"""Rectangle that defines widht and height"""
class Rectangle:
    def __init__(self, width=0, height=0):
        self._width = 0
        self._height = 0
        self.width = width
        self.height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._validate_dimensions(value, "width")
        self._width = value
    
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, value):
        self._validate_dimensions(value, "height")
        self._height = value
    
    def _validate_dimensions(self, value, dimension_name):
        if not isinstance(value, int):
            raise TypeError(f"{dimension_name} must be an integer")
        if value < 0:
            raise ValueError(f"{dimension_name} must a non-negative integer")
        

    def area(self):
        return self._width * self._height
    
rectangle = Rectangle(2, 7)
print(rectangle.area())
