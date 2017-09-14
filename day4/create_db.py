#! /usr/bin/env python3
# -*- coding : UTF-8 -*-
import sqlite3

try:
    # connect to database or create it if not existing
    db = sqlite3.connect('seriesBase.sqlite')

    # cursor object
    cursor = db.cursor()

    # create table
    cursor.execute('''create table personnage (
        id integer primary key,
        nom text,
        prenom text )''')

    # commit
    db.commit()

    # close stuff
    cursor.close()
    db.close()

except:
    print('Database creation error')
    exit(1)
