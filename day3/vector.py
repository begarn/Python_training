# create a class
from math import sqrt

class Vector:
    # constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __del__(self):
        print('The object' + str(self) + 'has been destroyed')

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
    print(str(v1))
    print(v1.longueur)
    print(v1.norme)
