#! /usr/bin/env python3
# -*- coding : UTF-8 -*-
import sqlite3

try:
    # connect to database or create it if not existing
    db = sqlite3.connect('seriesBase.sqlite')

    # cursor object
    cursor = db.cursor()

    # create table
    cursor.execute('''create table produit (
        id integer not null primary key autoincrement,
        nom text,
        prix real )''')

    # commit
    db.commit()

    # close stuff
    cursor.close()
    db.close()

except:
    print('Database creation error')
    exit(1)
