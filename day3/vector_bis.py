# create a class
from math import sqrt

class Vector:
    # constructor
    def __init__(self, x, y):
        self.__x = x # become private, need to define getter and setter to access it
        self.y = y

    def __del__(self):
        print('The object' + str(self) + 'has been destroyed')

    # 'x' attribute getter and setter
    def getX(self):
        return self.__x

    def setX(self, val):
        self.__x = val

    # => need it to continue to access the attribute by its name in the following code
    x = property(getX, setX)

    def __str__(self):
        """ Function to print object,
        here for mathematical format"""
        return "(" + str(self.x) + "," + str(self.y) + ")"

    def __add__(self, other):
        return Vector(x = self.x + other.x, y = self.y + other.y)

    @property # the following function become an attribute
    def norme(self):
        """Calculate the 'norme' of a vector"""
        return sqrt(self.x**2 + self.y**2)

    # alias
    longueur = norme

if __name__ == '__main__':
    v1 = Vector(2, 3)
    v1.x = 5
    print(v1)
    print(v1.norme)
