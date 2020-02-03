import datetime

from sys import getsizeof

def show_time (f):
    def wrapper(*args,**kwargs):
        start_time = datetime.datetime.now()
        a=f(*args, **kwargs)
        finish_time = datetime.datetime.now()
        report_time = finish_time - start_time
        print(report_time)
        return a
    return wrapper

def show_memory (f):
    def wrapper(*args,**kwargs):
        a=f(*args, **kwargs)
        memory_size = getsizeof(a)
        print(memory_size)
        return a
    return wrapper


@show_time
@show_memory

def list_num(a):
    num_list=[x for x in range(1,a+1) ]
    return num_list

@show_time
@show_memory

def gen_num(a):
    num_list=(x for x in range(1,a+1) )
    return num_list

@show_time
@show_memory

def gen_num2(a):
    for x in range(a):
        x += 1
        yield x


a=list_num(100000)

b=(gen_num(100000))

c=gen_num2(100000)
