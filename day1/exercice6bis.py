#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# exercice6bis.py
#

age = input('How old are you : ')

if not age.isnumeric() or int(age) < 0:
    print('wrong input')
    exit()

if int(age) < 18:
    print('Go back home children !')
else:
    print('Come in and have fun!')
