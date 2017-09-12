#! /usr/bin/env python3
# -*- coding : UTF-8 -*# pour spécifier le codage des caractères

def main():
    s1 = [ c for c in 'abc' ]
    s2 = [ c for c in 'de' ]

    print([ c1+c2 for c1 in s1 for c2 in s2 ])

if __name__ == '__main__':
    main()
