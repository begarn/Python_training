
#! /usr/bin/env python3
# -*- coding : UTF-8 -*# pour spécifier le codage des caractères
import random

def somme(mytuple):
    return sum(mytuple)

def main():
    mytuple = tuple(x for x in range(1, random.randint(1, 100)))
    print('the sum of each element of {} is: {}'.format(mytuple, somme(mytuple)))

if __name__ == '__main__':
    main()
