#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# exercice14.py
#
list1 = [ 'lapin', 'chat', 'chien', 'chiot', 'dragon', 'ornithorynque' ]
list2 = [ 'lapin', 'chat', 'chien', 'chiot' ]

list1.append('troll')

print(', '.join(list1))

for i in list2:
    list1.remove(i)

print(', '.join(list1))
