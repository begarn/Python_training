#! /usr/bin/env python3
# -*- coding : UTF-8 -*
from Card import Card
import random

class Deck:
    def __init__(self, empty = False):
        # self.deck = []
        # for color in Card.colors:
        #     for value in Card.values:
        #         self.deck.append(Card(color, value))
        if not empty:
            self.__deck = list(Card(color, value) for color in Card.colors for value in Card.values)
        else:
            self.__deck = []

    def getDeck(self):
        return self.__deck

    def setDeck(self, card):
        self.__deck.append(card)

    deck = property(getDeck, setDeck)

    def __str__(self):
        # return ', '.join(str(card) for card in self.__deck)
        return ', '.join(str(card) for card in self.deck)

    def mix(self):
        # return random.shuffle(self.__deck)
        return random.shuffle(self.deck)

    def take(self):
        try:
            # return self.__deck.pop(0)
            return self.deck.pop(0)
        except:
            raise Exception('The deck is empty')

if __name__ == '__main__':
    cg = Deck()
    c = cg.take()
    print(c)
    #print(len(cg.deck))
    # print(cg)
    # cg.mix()
    # print('\n' + str(cg))
    # try:
    #     while True:
    #         print(cg.take())
    # except Exception as e:
    #     print(str(e))
