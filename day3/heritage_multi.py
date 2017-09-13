class Animal:
    def __init__(self):
        print('I am an animal')

class Feline(Animal):
    def __init__(self):
        super().__init__()
        print('I am a feline')

class Domestic(Animal):
    def __init__(self):
        super().__init__()
        print('I am a domestic animal')

class Cat(Feline, Domestic):
    def __init__(self):
        super().__init__()
        print('I am a cat')

if __name__ == '__main__':
    mycat = Cat()
    print(isinstance(mycat, Cat))
    print(isinstance(mycat, Feline))
    print(isinstance(mycat, Animal))
    print(isinstance(mycat, Domestic))
