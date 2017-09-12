#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# exercice9.py
#
print('\'for\' style:')
for i in range(0,100,2):
    print(i)

print('\n\'while\' style:')
while True:
    print([i for i in range(0,100,2)])
    break
