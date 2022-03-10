'''a = 'b'
if ord(a)%2==0 :
    print("number is even")
else:
    print("number is not even")'''
"""WAP to check if given character is lowercase or not"""
'''value =input("enter the value")
if value.islower():
    print("it is lower case")
else:
    print("it is not lower")        or
    
value =input("enter the value")
if "a"<= value <="z":
    print("is lower")
else:
    print("is not lower")'''
"""the given string empty or not"""
'''a = input("enter the value")
if len(a)>0:
    print("it is not empty")
else:
    print("it is empty")              or

a = "jayu"
if a:
    print("it is iterable")
else:
    print("it is not iterable")'''

"""given value is default value or non default value"""
'''a = []
if a:
    print("it is not default value")
else:
    print("it is default value")'''

"""convert lower to upper and upper to lower"""

'''a = input("enter the value")
if a.islower():
    print(a.upper())
elif a.isupper():
    print(a.lower())
else:
    print("it is special")    or

a = input("enter the value")
if a.islower():
    print(a.swapcase())
elif a.isupper():
    print(a.lower())
else:
    print("it is special")'''
'''
n = 5
i = 0
while i<5:
    i+=1
    print(i)'''


"""custom sorting """
l = ["python", "java", "c", "ruby", "alpha"]
# print(sorted(l,key = len, reverse = True))

d = {"alpha":2, "beta":5, "gama":1, "anumerate":0}
# print(sorted(d.items()))

# "shortest", "*", "longest" == print(sorted(l, key = len))

# print(sorted(l, key = lambda item: item[len(item)//2]))

a = "Python is a programming language"
b = a.split()
shortest,*rest,longest = sorted(b, key=len)
# print([shortest, len(shortest)], [longest, len(longest)])

def last(ele):
    return ele[-1]

# print(sorted(b, key = last))
# print(sorted(b, key = lambda item : item[0]))

# print(sorted(b))
"""wap list element based on the last element the last char of each string"""
# print(sorted(b, key = lambda item : item[-1]))

d = {"gamil":5, "apple":3, "walmfgfgart":7, "flipkart":8 }
# print(dict(sorted(d.items(), key=lambda item: len(item[0][-1]))))

temperature = [("delhi", 32),("mumba",27),("kolkotta",30),("chennai",35)]
# print(sorted(temperature,key=lambda item: item[-1]))


# a = "hi how are you how is you life"
# b = a.split()
# d_count = {item:b.count(item) for item in b}
# res = sorted(d_count.items(), key=lambda char: char[-1])
# print(res)












