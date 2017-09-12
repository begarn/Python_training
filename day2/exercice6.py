#! /usr/bin/env python3
# -*- coding : UTF-8 -*# pour spécifier le codage des caractères

def main():
    print([ x + 3 for x in range(0, 5) if x > 2 ])

if __name__ == '__main__':
    main()
