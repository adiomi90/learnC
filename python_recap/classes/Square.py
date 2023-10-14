class Square:
    def __init__(self, height=0, width=0):
        self.height = height
        self.width = width

    
    @property
    def height(self):
        print("Retrieving the heights")

        return self.__height
    
    @height.setter
    def height(self, value):

        if value.isdigit():
            self.__height = value
        else:
            print("Please only digits")


    @property
    def width(self):
        print("Retriving the width")

        return self.__width
    
    @width.setter
    def width(self, value):
        if value.isdigit():
            self.__width = value
        else:
            print("please enter only digits")

    def getArea(self):
        return int(self.height) * int(self.__width)

height = input("Enter Height: ")
width = input("Enter width: ")
square = Square(height, width)


print("Height: ", square.height)
print("Width: ", square.width)
print("Area: ", square.getArea())


