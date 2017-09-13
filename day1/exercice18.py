#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# exercice18.py
#
list1 = [ 'hot', 'cold', 'moderate', 'icy', 'ardent' ]
with open('./temperature.txt', 'a') as fichier:
    fichier.write('\n')
    print(fichier.write('\n'.join(list1)))
