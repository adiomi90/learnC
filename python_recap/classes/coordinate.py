class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        x_diff_sq = (self.x-other.x) ** 2
        y_diff_sq = (self.y-other.y) ** 2
        return (x_diff_sq + y_diff_sq)
    
    def __str__(self):
        return f"<{self.x}, {self.y}"
    

point1 = Coordinate(1, 2)
point2 = Coordinate(3, 4)
print(point1.distance(point2))
