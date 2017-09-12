#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# exercice10bis.py
#

import random

magic_number = random.randint(0, 100)
print(magic_number)

while True:
    val1 = input('Try to find the number between 0-100 : ')

    if magic_number == int(val1):
        print('You win !')
        break
    elif magic_number < int(val1):
        print('The number is lower than your proposal, try again')
    else:
        print('The number is upper than your proposal, try again')
