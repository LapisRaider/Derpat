import math

class Vector2():
    def __init__(self):
        self.x = 0
        self.y = 0

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector2(self.x * scalar, self.y * scalar)

    def dot(self, other):
        self.x * other.x + self.y * other.y

    def length_squared(self):
        return self.x*self.x + self.y*self.y
    
    def length(self):
        return math.sqrt(self.x*self.x + self.y*self.y)

    def normalised(self):
        length = self.length()
        if (length == 0):
            return 0
        return Vector2(self.x/length, self.y/length)