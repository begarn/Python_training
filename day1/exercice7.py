#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# exercice7.py
#

devise = input('Enter the currency (E or $): ')
val = input('Enter the value: ')

if devise == 'E' or devise == '$':
    if devise == '$':
        print('{} $ is {:f} E'.format(val, float(val) * 0.834845))
    else:
        print('{} E is {:f} $'.format(val, float(val) * 1.19843))
else:
    print('wrong currency value')
