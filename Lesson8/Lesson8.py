import datetime
import tracemalloc
from sys import getsizeof


def show_time(f):
    def wrapper(*args, **kwargs):
        start_time = datetime.datetime.now()
        a = f(*args, **kwargs)
        finish_time = datetime.datetime.now()
        report_time = finish_time - start_time
        print(f'Время выполнения:{report_time}')
        return a

    return wrapper


def show_memory(f):
    def wrapper(*args, **kwargs):
        a = f(*args, **kwargs)
        memory_size = getsizeof(a)
        print(f'Данные в памяти: {memory_size} байт')
        return a

    return wrapper


def show_memory_2(f):
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        a = f(*args, **kwargs)
        memory_size = tracemalloc.get_traced_memory()
        print(f'Использование памяти:{memory_size[0]}байт MAX:{memory_size[1]}байт')
        tracemalloc.stop()
        return a

    return wrapper


@show_time
@show_memory
@show_memory_2
def list_num(a):
    print('Генератор списка ------------ ')
    num_list = [x for x in range(a)]
    return num_list


@show_time
@show_memory
@show_memory_2
def gen_num(a):
    print('Неявный генератор ------------ ')
    num_list = (x for x in range(1, a + 1))
    return num_list


@show_time
@show_memory
@show_memory_2
def gen_num2(a):
    print('Явный генератор ------------ ')
    for x in range(a):
        x += 1
        yield x


a = list_num(100000)

b = gen_num(100000)
print(next(b))
# for i in b:
#     print(i)

c = gen_num2(100000)
print(next(c))
#
# for i in c:
#     print(i)
