# def add(a, b,/):
#     return a+b
# print(add(1,2))


# def add(a, b):
#     print(a+b)
#
#
# add(1,2)
# print(add(1,2))

"""multiple argument return only string in reverse order"""
'''def rev(*args):
    a = []
    for i in args:
        if isinstance(i,str):
            a.append(i[::-1])
        else:
            a.append(i)
    return a

rev(1,1.2,"jau",4+4j,"hello")'''

""" if user inout not given print hai evryonee"""
# def di(msg="hai everyone"):
#     print(msg)
#

#
# di()

"""print the last number"""

# def last(num):
#      return num%10
#
#
# print(last(12348766))


# def iterable(*args):
#     d={}
#     for i in args:
#         if isinstance(i,(str, list, set, tuple, dict)):
#             d[len(i)]=i
#     return d
#
#
#
# print(iterable(1,2.3,4+5j,{"a":1, "b":2}, (1,2,3), {1,2,3}, "hello"))


# def per_sq(r1:int):
#     l = []
#     for i in range(r1):
#         r = int(i ** 0.5)
#         if r * r == i:
#             l.append(i)
#     return l
#
#
# print(per_sq(100))



'''def per_sq1(r1:int):
    l = []
    i = 1
    while i < r1:
        r = int(i ** 0.5)

        if r * r == i:

            l.append(i)
        i += 1

    return l
    


print(per_sq1(100))'''

'''a = "hello world"
d = {}
for i in a:
    d[i] = a.count(i)
print(d)'''
'''printing 10 to 1 using recursion'''
'''def count(s,e):
    if s<e:
        return
    print(s)
    count(s-1, e)
count(10, 1)'''
'''a = 1234
t = 0
while a > 0:
    rem = a%10
    t = rem + t
    a = a//10
print(t)'''
'''add of the digit'''
'''def sum(a, t = 0):
     if a > 0:
        rem = a % 10
        t = rem + t
        a//=10
        return sum(a, t)
     else:
         return t

print(sum(1234))'''
'''
last = lambda i : i%10
print(last(123))

pal = lambda a : a==a[::-1]
print(pal('amma'))


a = lambda n :f"{n} is a even number" if n%2 == 0 else f"{n} it is odd number"
print(a(6))

ax = [1,2,3,4,4,4l,67]
bx = lambda n :f"{n} is a even number" if n%2 == 0 else f"{n} it is odd number"'''

"""functions that returns the list of even range from 1 to 51"""

def value(end, start = 0):
    l = []
    for i in  range(start, end+1):
        if i%2 == 0:
            l.append(i)
    return l


print(value(50, 30))

















