#! /usr/bin/env python3
# -*- coding : UTF-8 -*# pour spécifier le codage des caractères

def main():
    ponctuation = (";", ",", ".", ":", "\"", "'","—", "?", "!", "-")
    t = set()

    with open('./chanson.txt', 'r') as fd:
        s = fd.read().lower()
        
    for p in ponctuation:
        s = s.replace(p,' ')

    for w in s.split():
        t.add(w)
    print(t)

if __name__ == '__main__':
    main()
