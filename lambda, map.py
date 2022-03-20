'''a = "ABCdsfd"
b = "XYZhdhe"
res = ""
c = b[::-1]
if len(a) == len(c):
    for i in range(len(a)):
        res += a[i] + c[i]
else:
    print('not of same length')
print(res)

a = ["abg","jhhhb"]
res = list(map(tuple,a))
print(res)

"""squire and keep it in list"""

a = [1,2,3,4,6,6,78,9,88,88, 64]
#b = lambda a : a**2
#print(list(map(b,a)))

even_ind = lambda ab : (ab**2) if a.index(ab) % 2 == 0 else None
d = list(map(even_ind, a))

def p(i):
    return i
# print(list(filter(p, d)))'''


'''wap to get length of each word'''

a = "hello world welcome to python"
b = a.split()
# def length(a):
#     return len(b)


# print(length(b))
res = map(len, b)
print(list(res))















