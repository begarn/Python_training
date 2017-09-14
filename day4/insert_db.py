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

    # insertion
    for data in persos:
        cursor.execute('insert into personnage(nom, prenom) values(?,?)', data)

    # commit
    db.commit()

    # close stuff
    cursor.close()
    db.close()

except:
    print('Database creation error')
    exit(1)
