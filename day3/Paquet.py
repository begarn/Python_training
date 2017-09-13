#! /usr/bin/env python3
# -*- coding : UTF-8 -*
from Card import Card
from Deck import Deck

class Paquet(Deck):
    def __init__(self):
        super().__init__(True)

    def add(self, card):
        self.deck.append(card)

if __name__ == '__main__':
    p = Paquet()
    print(p)
    p.add(Card(1,4))
    print(p)
    print(p.take())
    print(p)
