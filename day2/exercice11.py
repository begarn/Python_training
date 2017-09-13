#! /usr/bin/env python3
# -*- coding : UTF-8 -*# pour spécifier le codage des caractères
def pile(*args):
    return [ x for x in args ]

def empile(element):
    lifo.append(element)

def depile():
    lifo.pop()

def main():
    global lifo
    lifo = pile(1,2,3,4)
    empile(5)
    depile()
    depile()
    print(lifo)

if __name__ == '__main__':
    main()
