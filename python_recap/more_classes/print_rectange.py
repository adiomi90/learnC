class Rectangle:
    number_of_instance = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self._width = 0
        self._height = 0
        self.width = width
        self.height = height
        Rectangle.number_of_instance += 1

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
    
    def __str__(self):
        "present the character stored in print_symbol"
        result = ""
        for _n in range(self._height):
            result +=  str(self.print_symbol) * self.width + "\n"
        return result
    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})" 

    def __del__(self):
        Rectangle.number_of_instance -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        """
        Return the rectangle with the greater area
            Args:
                rect_1: first rectangle
                rect_2: second rectange
            Raises:
                TypeError: if not a rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectange")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectange")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
    
    @classmethod
    def square(cls, size=0):
        return cls(size, size)



my_rectangle_1 = Rectangle(8, 4)
print(my_rectangle_1)
print("--")
my_rectangle_1.print_symbol = "&"
print(my_rectangle_1)
print("--")
my_rectangle_2 = Rectangle(2, 1)
print(my_rectangle_2)
print("--")
Rectangle.print_symbol = "C"
print(my_rectangle_2)
print("--")

my_rectangle_3 = Rectangle(7, 3)
print(my_rectangle_3)

print("--")

my_rectangle_3.print_symbol = ["C", "is", "fun!"]
print(my_rectangle_3)

print("--")



""" 
        

my_rectangle = Rectangle(2, 4)
print(str(my_rectangle))
print("--")
print(my_rectangle)
print("--")
print(repr(my_rectangle))
print("--")
print(hex(id(my_rectangle)))
print("--")

# create new instance based on representation
new_rectangle = eval(repr(my_rectangle))
print(str(new_rectangle))
print("--")
print(new_rectangle)
print("--")
print(repr(new_rectangle))
print("--")
print(hex(id(new_rectangle)))
print("--")

print(new_rectangle is my_rectangle)
print(type(new_rectangle) is type(my_rectangle))
 """
