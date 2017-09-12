#! /usr/bin/env python3
# -*- coding : UTF-8 -*# pour spécifier le codage des caractères

def main():
    X = { 'a', 'b', 'c', 'd' }
    Y = { 's', 'b', 'd' }

    print('X: {}'.format(X))
    print('Y: {}'.format(Y))
    print('Is \'c\' in X: {}'.format('c' in X))
    print('Is \'a\' in Y: {}'.format('a' in Y))
    print('X-Y: {}'.format(X.difference(Y)))
    print('Y-X: {}'.format(Y.difference(X)))
    print('X union Y: {}'.format(X.union(Y)))
    print('X inter Y: {}'.format(X.intersection(Y)))

if __name__ == '__main__':
    main()
