#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# exercice17.py
#
list1 = [ "chaud", "froid", "tempéré", "glacial", "brûlant" ]
with open('./temperature.txt', 'w') as fichier:
    print(fichier.write('\n'.join(list1)))
