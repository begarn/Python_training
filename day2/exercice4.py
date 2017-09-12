#! /usr/bin/env python3
# -*- coding : UTF-8 -*# pour spécifier le codage des caractères
def mydictionnary(**dico):
    return dico


def main():
    dico = {
    'a': 'alphabet',
    'b': 'byte',
    'c': 'chocolate'
    }

    print(mydictionnary(**dico))

if __name__ == '__main__':
    main()
