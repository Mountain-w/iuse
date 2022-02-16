def solution_2978(price, customer, vip, blacklist):
    if customer in vip:
        return f'{price * 0.7:.2f}'
    elif customer not in blacklist:
        return price
    else:
        return -1


def solution_2990(arr):
    discount = []
    for i in arr:
        if i[0] not in ['j', 'z', 'd', 'f', 'h']:
            continue
        discount.append(i)
    return discount


def solution_2991(arr):
    arr = [int(a) for a in arr]
    return f'{arr[0] / arr[1] * (arr[2] + arr[3]):.2f}'


def solution_2992(s):
    s_split = s.split('\n')
    get_name = s_split[0].split(' ')[1][:-1]
    send_name = s_split[-1]
    return f'{send_name},{get_name}'


def solution_2996(arr):
    ans = 0
    for a in arr:
        ans += max(a)
    return f'{ans / len(arr):0.2f}'


def get_goods(goods: list) -> str:
    # Please write your code here
    goods_sorted = sorted(goods, key=lambda x: (x[1], x[0]))
    return goods_sorted[-1][0]


def solution_3006(num):
    return f'/output/{num}.txt'


def print_avg(*args, **kwargs) -> str:
    name = kwargs['student_name']
    age = kwargs['student_age']
    avg = sum(args) / len(args)
    return f"name: {name}, age: {age}, avg: {avg:.2f}"


def print_avg_error(*args, **kwargs) -> str:
    name = kwargs.get('student_name', None)
    age = kwargs.get('student_age', None)
    if name is None or age is None:
        return 'Incomplete keywords'
    if len([param for param in args if not isinstance(param, int)]) != 0:
        return "It's not all about numbers"
    avg = sum(args) / len(args)
    return f"name: {name}, age: {age}, avg: {avg:.2f}"


def get_write_csv(lists):
    text = ''
    for l in lists:
        text += ','.join([str(i) for i in l]) + '\n'
    return text


def solution_2965(n1, n2, nlist):
    num1_arr = []
    num2_arr = []
    for a in nlist:
        num1_arr.append(a if a % n1 == 0 else 0)
        num2_arr.append(a if a % n2 == 0 else 0)
    return [num1_arr, num2_arr]


def solution_2966(n1, n2, nlist):
    comm = []
    for a in nlist:
        comm.append(a if a % n1 == 0 and a % n2 == 0 else 0)
    return comm


def soluion_3016(blacklist, customers):
    for customer in customers:
        if customer in blacklist:
            return f'Alert, {customer} is on the blacklist.'
    return 'Welcome to the next visit'


def solution_2937(num):
    return num & (-num)


def find_n(list_1: list, n) -> list:
    from collections import Counter
    max_n_counts = Counter(list_1).most_common(n)
    return [max_n_count[0] for max_n_count in max_n_counts]