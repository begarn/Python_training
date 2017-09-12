#! /usr/bin/env python3
# -*- coding : UTF-8 -*# pour spécifier le codage des caractères
def isempty():
    return len(fifo) == 0

def enfiler(element):
    fifo.append(element)

def defiler():
    fifo.pop(0)

def print_fifo():
    print(fifo)

def main():
    global fifo
    fifo = list()
    print('isempty: {}'.format(isempty()))
    enfiler(1)
    enfiler(3)
    enfiler(2)
    print_fifo()
    print('isempty: {}'.format(isempty()))
    defiler()
    print_fifo()

if __name__ == '__main__':
    main()
