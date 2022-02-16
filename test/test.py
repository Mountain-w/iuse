class TestError(Exception):
    pass


# t = TestError('ok', '3')
# print(str(t))


class Person(Exception):
    def __init__(self, *args, **kwargs):  # real signature unknown
        pass


p1 = Person('ok', '3')
print(p1)
