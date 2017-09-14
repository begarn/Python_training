#! /usr/bin/env python3
# -*- coding : UTF-8 -*

class Card:
    values = {
        2: '2',
        3: '3',
        4: '4',
        5: '5',
        6: '6',
        7: '7',
        8: '8',
        9: '9',
        10: '10',
        11: 'Valet',
        12: 'Dame',
        13: 'Roi',
        14: 'As'
    }

    colors = {
        0: 'Coeur',
        1: 'Careau',
        2: 'Trefle',
        3: 'Pique'
    }

    def __init__(self, color, value):
        if not isinstance(color, int) or not color in self.__class__.colors:
            raise Exception('Wrong type or value')
        if not isinstance(value, int) or not value in self.__class__.values:
            raise Exception('Wrong type or value')
        self.__color = color
        self.__value = value

    def __str__(self):
        return self.__class__.values[self.__value] + ' de ' + self.__class__.colors[self.__color]

    def display(self):
        print(self.__class__.values[self.__value] + ' de ' + self.__class__.colors[self.__color])

if __name__ == '__main__':
    c1 = Card(0, 14)
    c1.display()
    print(c1)


    #c2 = Card(5,4)
