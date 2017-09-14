#! /usr/bin/env python3
# -*- coding : UTF-8 -*-
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    price = Column(Integer)

if __name__ == '__main__':
    try:
        engine = create_engine('sqlite:///seriesBase.sqlite')
        DBSession = sessionmaker(bind=engine)
        session = DBSession()

        p = session.query(Product).all()
        for product in p:
            print(product.name + '|' + str(product.price))

    except Exception as e:
        print('Database creation error')
        print(str(e))
        exit(1)
