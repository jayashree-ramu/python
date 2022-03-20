
from time import sleep
from time import time
"""decorate the length of the function"""

"""def my_decorator_func(func):
    def wrapper_func(*args, **kwargs):
        res = (len(args), len(kwargs))
        return res
    return wrapper_func

@my_decorator_func
def my_func(*args, **kwargs):
    return args, kwargs


print(my_func(["hello", "hai","fine"],{"a":1, "b":2, "c":3}, (1, 2, 3), a ={1, 2, 3, 4}, b = 123))"""
"""parameterized delay"""
# def _delay(n):
#     def delay(func):
#         def wrapper(*args, **kwargs):
#             sleep(n)
#             return func(*args, **kwargs)
#         return wrapper
#     return delay
#
# @_delay(3)
# def add(a, b):
#     return a+b
#
# print(add(5, 7))
#
# @_delay(10)
# def mul(a, b):
#     return a*b
#
# print(mul(1,2))

"""reverse the string"""

# def _reverse(func):
#     l = []
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         for item in res:
#             if isinstance(item, str):
#                 l.append(item[::-1])
#         print(l)

#         return res
#     return wrapper
#
# @_reverse
# def string(*args):
#     return args
#
# print(string("hello", "hai", (1,2,3,4), "jayu", {"a":1, "b":2}, [1, 2, 3]))
#
# """execute function for 3 times"""
#
# def _times(n):
#     def times_(func):
#         def wrapper(*args, **kwargs):
#             res = func(*args, **kwargs)
#             for i in range(n):
#                 print(res)
#         return wrapper
#     return times_


# @_times(3)
# def string(a):
#     return a
#
#
# string("hello world")
#
# @_times(5)
# def hv(*args, **kwargs):
#     return args, kwargs
#
# hv("hello world" , a = (1,2,3))


"""decorate the execution time taken for execution"""
# def _outer(n):
#     def outer(func):
#         def wrapper(*args, **kwargs):
#             start = time()
#             sleep(n)
#             func(*args, **kwargs)
#             end = time()
#             print(f"the execution time of function {func.__name__} is {end-start} seconds")
#         return wrapper
#     return outer
#
# @_outer(1)
# def add(a, b):
#     return a+b
#
#
# add(1, 2)
#
# @_outer(3)
# def mul(a,b):
#     return a*b
#
# mul(1,2)

"""count the number of argument passed to a function"""

# def count_(func):
#     def wrapper(*args, **kwargs):
#         count = 0
#         for _ in args:
#             count += 1
#         for _ in kwargs:
#             count += 1
#         print(count)
#         return func(*args, **kwargs)
#     return wrapper
#
# @count_
# def add(a,b,c,d,r):
#     return a+b+c,d,r
#
# add(1,2,3, d = 6, r = 2)

"""aways to get the positive answer"""
# def positi(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         if isinstance(res, (int, float, complex)):
#             return abs(res)
#         return res
#     return wrapper
#
# @positi
# def sub(a,b):
#     return a-b
#
# print(sub(1, 4))
#g
# @positi
# def mul(a,b):
#     return a*b
#
# print(mul(1,-5))
#
# @positi
# def st(a):
#     return a
#
# print(st("hello world"))



# @positi
# def mul(a,c,d):
#     return a*d*c
#
# mul(1,2,3)

def in_(func):
    def c(*args, **kwargs):
        print("*some*")
        func(*args, **kwargs)
        print("*some*")
    return c


def inn_(func):
    @in_
    def c(*args, **kwargs):
        print("*more*")
        func(*args, **kwargs)
        print("*more*")
    return c

@in_
@inn_
def d(a):
    print(a)

d("hello")




































