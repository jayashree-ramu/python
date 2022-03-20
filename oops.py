"""__init__ methon"""
"""
class computer:

    def __init__(self,cpu, ram):
        self.cpu = cpu
        self.ram = ram


    def config(self):
        print("config is",self.cpu, self.ram)



com1 = computer("i5", 16)
com2 = computer("reyzen 3", 8)

com1.config()
com2.config()

"""

# class computer:
#     pass
#
#
# c1 = computer()
# c2 = computer()
#
# print(id(c1))
# print(id(c2))

# class computer:
#
#     def __init__(self):
#         self.name = "janu"
#         self.age = 20
#
# c1 = computer()
# c2 = computer()
# c1.name = "pinku"
# c1.age = 30
#
# print(c1.name, c1.age)
# print(c2.name, c2.age)

'''WAf to print n number pf prime numbers 
def prime(start,end):
    for n in range(start, end+1):
        if n > 1:
            for item in range(2, n):
                if n%item == 0:
                    break
            else:
                print(n)

prime(1,10)'''

#
# for row in range(ord("a"),ord("e")+1):
#     for col in range(ord("a"), row+1):
#         print(chr(col), end=" ")
#     print()
#
# l = range(ord('A'),ord('J')+1)
# print(l)
# l1 = []
# for items in l:
#     l1.append(chr(items))
# print(l1)
#
# l2 = l1[::-1]
# print(l2)
#
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(l2.pop(), end=' ')
#     print()
# num = 153
# a = str(num)
# b = len(a)
# res  = 0
# for iten in a:
#     if num == res:
#         print(f"{num} is amstrong")
#         break
#
#     else:
#         print("not a amstrong number")
#         break



num = 153
leng = len(str(num))
last =  num % 10
a = last ** leng
res = num // 10

def amg(n, a = 0):

    while n > 0 :
        leng = len(str(n))
        last = n % 10
        a += last ** leng
        n = n // 10

    print(a)
amg(153)


























