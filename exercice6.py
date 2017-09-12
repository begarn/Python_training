#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# exercice6.py
#
str1 = input('Enter the first string: ')
str2 = input('Enter the second string: ')

# if len(str1) > len(str2):
#     print('The longest string is : ',str1)
# else:
#     print('The longest string is : ',str2)
print('The longest string is : ', max(len(str1), len(str2)))
