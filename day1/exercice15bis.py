#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# exercice15bis.py
#

import random

list1 = []
magic_number = random.randint(0, 100)
print(magic_number)

while True:
    val1 = input('Try to find the number between 0-100 : ')
    list1.append(val1)

    if magic_number == int(val1):
        print('You find the right number in %d tries !' % len(list1) )
        break
    elif magic_number < int(val1):
        print('The number is lower than your proposal, try again')
    else:
        print('The number is upper than your proposal, try again')
