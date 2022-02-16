
class Sample:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __gt__(self, other):
        name = other.name
        print("I am ", name)
        return self.score > other.score

    def __lt__(self, other):
        name = other.name
        print("I am ", name)
        return self.score < other.score


s1 = Sample('A', 20)
s2 = Sample('B', 10)
print(s1 > s2)
print('*' * 20)
print(s1.__gt__(s2))
print('*' * 20)
print(s1 < s2)
print('*' * 20)
print(s1.__lt__(s2))
