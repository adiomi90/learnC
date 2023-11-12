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
        self._validate_value("width", value)
        self._width = value

    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, value):
        self._validate_value("height", value)
        self._height =  value

    def _validate_value(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value < 0:
            raise ValueError(f"{name} must be >= 0")
        
    def area(self):
        return self._height * self._width
    
    def perimeter(self):
        if self._width == 0 or self._height == 0:
            return 0
        return 2 * (self._height + self._width)
    
rectange = Rectangle(7, -2)
print(rectange.perimeter())
print(rectange.area())
