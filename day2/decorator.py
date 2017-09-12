#! /usr/bin/env python3
# -*- coding : UTF-8 -*# pour spécifier le codage des caractères

# une fonction qui va decorer une autre
def decorator(function):
    def fake(name): # meme arguments que la fonction a decorer
        print('Function call ' + function.__name__ + ' with parameters ' + name)
        return function(name)
    return fake

@decorator
def sayhello(name):
    return 'Hello ' + name

@decorator
def saythankyou(name):
    return 'Thank you ' + name

print(sayhello('Dupont'))
print(saythankyou('Dolto'))
