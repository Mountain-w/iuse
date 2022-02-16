class Person:
    def __init__(self, name):
        self.name = name
        print("Hello")


class Man(Person):
    pass


man1 = Man("Jack")
print(isinstance(man1, object))
