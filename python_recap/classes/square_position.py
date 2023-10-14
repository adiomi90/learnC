class Square:
    def __init__(self, size=0, position=(0,0)):
        self.__size = size
        self.__position = position


    @property
    def size(self):
        return self.__size
    

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            return TypeError("value size be an integer")

        if value < 0:
            return ValueError("size must be an integer")
        

    @property
    def position(self):
        return self.__position
    
    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2 or all(not isinstance(i, int) and i >=0 for i in value):
           raise TypeError("position must be a tuple of 2 postive integer") 
        self.__position = value

    def area(self):
        return self.__size ** 2
    
    def my_print(self):
        if self.__size == 0:
            print()
        
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.size):
            print(" " * self.__position[0] , "#" * self.__size)

my_square_1 = Square(3)
my_square_1.my_print()

print("--")

my_square_2 = Square(3, (1, 1))
my_square_2.my_print()

print("--")

my_square_3 = Square(3, (3, 0))
my_square_3.my_print()

print("--")

























































































""" def __init__(self, size=0, position=(0, 0)):
        
        Initialize the square

        Args: 
           size (int) : The size of the square
           position (tuple): The position of the square(x, y)
        
        self.__size = size
        self.__position = position

    @property
    def size(self) -> int:
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value: tuple):
        if not isinstance(value, tuple) or value != 2 or all(not isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be at tuple of 2 postive integers")
        self.__position = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print("")

        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
"""

