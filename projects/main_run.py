from generate_var import Case_generator
from generate_file import FileGenerator
from solution import *
import random


def main_2978(num):
    price = random.randint(20, 1000)
    vip = Case_generator.generate_name_arr(random.randint(5, 10))
    blacklist = Case_generator.generate_name_arr(random.randint(2, 5))
    weight = random.random()
    if 0 < weight < 0.3:
        customer = vip[random.randint(0, len(vip) - 1)]
    elif 0.3 <= weight < 0.6:
        customer = blacklist[random.randint(0, len(blacklist) - 1)]
    else:
        customer = Case_generator.generate_name_str()
    FileGenerator.make_file(
        num,
        [price,
         "'" + customer + "'",
         vip,
         blacklist
         ],
        'in'
    )
    result = solution_2978(price, customer, vip, blacklist)
    FileGenerator.make_file(num, [result], 'out')


def main_2990(num):
    arr = Case_generator.generate_word_arr(random.randint(15, 200))
    FileGenerator.make_file(num, [arr], 'in')
    result = solution_2990(arr)
    FileGenerator.make_file(num, [result], 'out')


def main_2991(num):
    arr = Case_generator.generate_int_arr(1, 100, 4)
    FileGenerator.make_file(
        num,
        [Case_generator.generate_has_seq(arr, 'list')],
        'in'
    )
    result = solution_2991(arr)
    FileGenerator.make_file(num, [result], 'out')


def main_2992(num):
    s = f"Dear {Case_generator.generate_str(random.randint(4, 7))}:\n\t{Case_generator.generate_str(4)} " \
        f"{Case_generator.generate_str(5)} {Case_generator.generate_str(4)} {Case_generator.generate_str(10)}" \
        f" {Case_generator.generate_str(9)} " \
        f"{Case_generator.generate_str(8)}\n{Case_generator.generate_str(random.randint(6, 10))}"
    FileGenerator.make_file(num, [repr(s)], 'in')
    result = solution_2992(s)
    FileGenerator.make_file(num, [result], 'out')
    print(s)


def main_2996(num):
    arrs = []
    for i in range(10):
        arrs.append(Case_generator.generate_int_arr(1, 100, 5))
    FileGenerator.make_file(num, [Case_generator.generate_has_seq(arrs, 'list')], 'in')
    result = solution_2996(arrs)
    FileGenerator.make_file(num, [result], 'out')


def main_3001(num):
    arr = []
    for i in range(10):
        arr.append((Case_generator.generate_random_word(), random.randint(8, 100)))
    FileGenerator.make_file(
        num,
        [arr],
        'in'
    )
    result = get_goods(arr)
    FileGenerator.make_file(
        num,
        [result],
        'out'
    )


def main_3006(num):
    arr = Case_generator.generate_int_arr(30, 200, 6)
    arr.extend(Case_generator.generate_word_arr(5))
    result = solution_3006(num)
    FileGenerator.make_file(
        num,
        ["'" + result + "'", arr],
        'in'
    )
    FileGenerator.make_file(
        num,
        [arr],
        'out'
    )


def main_3007(num):
    path = f"'/output/{num}.json'"
    name = Case_generator.generate_name_str()
    age = random.randint(3, 89)
    dict_1 = {'name': name, 'age': age}
    FileGenerator.make_file(
        num,
        [path, dict_1],
        'in'
    )
    dict_1['age'] = 18
    FileGenerator.make_file(
        num,
        [dict_1],
        'out'
    )
    print('*' * 20)
    print(path, dict_1)


def main_3008(num):
    gardents = Case_generator.generate_int_arr(50, 100, random.randint(5, 10))
    student = {
        'student_name': Case_generator.generate_name_str(),
        'student_age': random.randint(18, 23)
    }
    for i in range(random.randint(3, 9)):
        student[Case_generator.generate_random_word()] = Case_generator.generate_random_word()
    FileGenerator.make_file(
        num,
        [gardents, student],
        'in',
    )
    result = print_avg(*gardents, **student)
    print(gardents, student, result)
    FileGenerator.make_file(
        num,
        [result],
        'out',
    )


def main_3011(num):
    gardents = Case_generator.generate_int_arr(50, 100, random.randint(5, 10))
    random_int = random.random()
    student = {}
    if random_int < 0.3:
        student['student_name'] = Case_generator.generate_name_str()
    elif 0.3 <= random_int < 0.5:
        student['student_age'] = random.randint(18, 23)
    else:
        student['student_name'] = Case_generator.generate_name_str()
        student['student_age'] = random.randint(18, 23)
    for i in range(random.randint(3, 9)):
        student[Case_generator.generate_random_word()] = Case_generator.generate_random_word()
    random_int = random.random()
    if random_int < 0.5:
        gardents.append(Case_generator.generate_random_word())
    FileGenerator.make_file(
        num,
        [gardents, student],
        'in',
    )
    result = print_avg_error(*gardents, **student)
    print('*' * 20)
    print(gardents, student, result, sep='\n')
    print('*' * 20)
    FileGenerator.make_file(
        num,
        [result],
        'out',
    )


def main_3012(num):
    out_path = f"'/output/{num}.csv'"
    students = [['name', 'class', 'age']]
    for i in range(random.randint(8, 40)):
        students.append([
            Case_generator.generate_name_str(),
            str(random.randint(1, 10)),
            random.randint(19, 25),
        ])
    FileGenerator.make_file(
        num,
        [out_path, students],
        'in'
    )
    students[0][0] = 'student_name'
    FileGenerator.make_file(
        num,
        [get_write_csv(students)],
        'out'
    )
    print('*' * 20)
    print(out_path, students, get_write_csv(students), sep='\n')


def main_2965(num):
    num_1 = random.randint(1, 9)
    num_2 = random.randint(1, 9)
    num_list = Case_generator.generate_int_arr(10, 900, random.randint(8, 20))
    FileGenerator.make_file(
        num,
        [num_1, num_2, num_list],
        'in'
    )
    result = solution_2965(num_1, num_2, num_list)
    FileGenerator.make_file(
        num,
        [result],
        'out'
    )


def main_2966(num):
    num_1 = random.randint(1, 9)
    num_2 = random.randint(1, 9)
    num_list = Case_generator.generate_int_arr(10, 900, random.randint(8, 20))
    FileGenerator.make_file(
        num,
        [num_1, num_2, num_list],
        'in'
    )
    result = solution_2966(num_1, num_2, num_list)
    FileGenerator.make_file(
        num,
        [result],
        'out'
    )


def main_3016(num):
    blacklist = Case_generator.generate_name_arr(random.randint(3, 5))
    customers = Case_generator.generate_name_arr(random.randint(14, 40))
    randnum = random.random()
    if randnum < 0.5:
        for b in blacklist:
            if b in customers:
                customers.remove(b)

    FileGenerator.make_file(
        num,
        [blacklist, customers],
        'in'
    )
    result = soluion_3016(blacklist, customers)
    FileGenerator.make_file(
        num,
        [result],
        'out'
    )
    print('*' * 20)
    print(blacklist, customers, result, sep='\n')


def main_2937(num):
    randomnum = random.randint(0, 1000)
    FileGenerator.make_file(
        num,
        [randomnum],
        'in'
    )
    result = solution_2937(randomnum)
    FileGenerator.make_file(
        num,
        [result],
        'out'
    )


def main_3025(num):
    list_length = random.randint(1, 20)
    list_1 = Case_generator.generate_int_arr(0, 300, list_length)
    for i in range(random.randint(0, list_length // 2)):
        list_1.extend([list_1[random.randint(0, list_length - 1)]] * random.randint(2, 5))
    if len(list_1) == 1:
        n = random.randint(0, 1)
    else:
        n = random.randint(1, list_length - 1)
    FileGenerator.make_file(
        num,
        [list_1, n],
        'in'
    )
    FileGenerator.make_file(
        num,
        [find_n(list_1, n)],
        'out'
    )


def main_2973(num):
    word_1 = Case_generator.generate_random_word()
    word_2 = Case_generator.generate_random_word()
    FileGenerator.make_file(
        num,
        [word_1.encode(), "'" + word_2 + "'"],
        'in'
    )
    FileGenerator.make_file(
        num,
        [word_1, word_2.encode()],
        'out'
    )


def main_2925(num):
    num1 = random.randint(0, 100)
    word = Case_generator.generate_random_word()
    FileGenerator.make_file(
        num,
        [num1, "'" + word + "'"],
        'in'
    )
    FileGenerator.make_file(
        num,
        [(num1, word), type(())],
        'out'
    )


def main_2920(num):
    word = Case_generator.generate_random_word()
    FileGenerator.make_file(
        num,
        ["'" + word + "'"],
        'in'
    )
    FileGenerator.make_file(
        num,
        ["'" + word + "'"],
        'out'
    )


def main_2947(num):
    list_1 = Case_generator.generate_int_arr(0, 500, random.randint(10, 20))
    randnum = random.random()
    num_1 = random.randint(0, 500)
    if randnum >= 0.5:
        list_1.append(num_1 - 1)
    FileGenerator.make_file(
        num,
        [num_1, list_1],
        'in'
    )
    FileGenerator.make_file(
        num,
        [(num_1 - 1) in list_1],
        'out'
    )


def main_2982(num):
    origin_arr = Case_generator.generate_int_arr_noduplicate(0, 200, random.randint(5, 10))
    randnum = random.randint(0, len(origin_arr) - 1)
    origin_num = origin_arr[randnum]
    for i in range(len(origin_arr)):
        if i == randnum:
            continue
        origin_arr.extend([origin_arr[i] for _ in range(random.randrange(2, 8, 2)-1)])
    origin_arr.extend([origin_arr[randnum] for _ in range(random.randrange(0, 8, 2))])
    random.shuffle(origin_arr)
    ans = 0
    for i in origin_arr:
        ans ^= i
    print(ans, ans in origin_arr)
    print(origin_num)
    if ans == origin_num:
        print(origin_arr)
        print('success')
        print('*' * 20)
        FileGenerator.make_file(
            num,
            [origin_arr],
            'in'
        )
        FileGenerator.make_file(
            num,
            [ans],
            'out'
        )

    else:
        print(origin_arr)
        print('error')
        print('*' * 20)



if __name__ == '__main__':
    for i in range(1, 11):
        main_2990(i)
        # break
