#! /usr/bin/env python3
# -*- coding : UTF-8 -*-
import sqlite3

# data to add
persos = [('Skywalker', 'Luke'), ('Skywalker','Anakin'), ('Solo','Han')]

try:
    # connect to database or create it if not existing
    db = sqlite3.connect('seriesBase.sqlite')

    # cursor object
    cursor = db.cursor()

    # fetch data
    cursor.execute('select * from personnage')
    for row in cursor:
        print('{} | {:15} | {:15}'.format(*row))

    # close stuff
    cursor.close()
    db.close()

except:
    print('Database creation error')
    exit(1)
