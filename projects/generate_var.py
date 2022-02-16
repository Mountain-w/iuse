import random
from random import randint


class Case_generator:
    with open('names.txt', 'r') as f:
        names = eval(f.readline())
    with open('word5506.txt', 'r') as f:
        words = eval(f.readline())

    @classmethod
    def generate_name_str(cls):
        return cls.names[randint(0, len(cls.names) - 1)]

    @classmethod
    def generate_random_word(cls):
        return cls.words[randint(0, len(cls.words) - 1)]

    @classmethod
    def generate_name_arr(cls, arr_len):
        arr = []
        for i in range(arr_len):
            name = cls.generate_name_str()
            while name in arr:
                name = cls.generate_name_str()
            arr.append(name)
        return arr

    @classmethod
    def generate_word_arr(cls, arr_len):
        arr = []
        for i in range(arr_len):
            name = cls.generate_random_word()
            while name in arr:
                name = cls.generate_random_word()
            arr.append(name)
        return arr

    @classmethod
    def generate_int_arr(cls, start, end, arr_len):
        arr = []
        for i in range(arr_len):
            arr.append(randint(start, end))
        return arr

    @classmethod
    def generate_int_arr_noduplicate(cls, start, end, arr_len):
        arr = []
        for i in range(arr_len):
            num = randint(start, end)
            while num in arr:
                num = randint(start, end)
            arr.append(num)
        return arr


