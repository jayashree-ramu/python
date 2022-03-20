"""index and its corresponding element in the list"""

li = ["hello world", "hello universe", (1, 2, 3, 4), {1,2,3}, {"a":1, "B":2}]
# for item in range(len(li)):
 #  print(item,"---->",li[item])

# for index,char in enumerate(li):
    # print(index,"--->",char)

# for item in range(len(li)):
#     print("index is",item)
#     print("element", li[item])
#
"""print element in list in the reverse order"""
# print(li[::-1])

# for item in reversed(li):
#     print(item, end=" ")

# rev = (item[::-1] for item in li)
# print(rev)

# for item in range(len(li)-1,-1,-1):
#     print((li[item]), end = " ")

# for item in li[::-1]:
#     print(item, end=" ")

"""atlernative element in list"""

# for item in range(0,len(li),2):
#     print(li[item], end=" ")

# for item in li[::2]:
#     print(item, end=" ")

# for item in range(len(li)):
#     if item%2 != 0:
#         print(li[item], end=" ")

"""print length og each element in the list"""
# for item in li:
#     print((item, len(item)))

# a =
"""wap even length item"""
# for item in li:
#     if len(item)%2 == 0:
#         print(item)
#     else:
#         print(item[::-1])

"""1st digit even or odd"""
# a = 3232
# b = str(a)
# if int(b[0])%2 == 0:
#     print("it is even")
# else :
#     print("its odd")


# b = "o"
# d = {}
# if b.lower() in "aeiou":
#     # d[b]=ord(b)
#     d.setdefault(b,ord(b))
# else:
#     print("not a vowel")
#
# print(d)


# a = "anuj"
# i = 0
# while len(a)>i:
#     print(a[i], end=" ")
#     i+=1

# s = "python"
# for item in s[::2]:
#     print(item)

# s = "@12helo34hsi78"
# count = 0
# for item in s:
#     if "0"<=item<="9":
#         count += 1
#
# print(count)

# a = "12@fe#f4f*&&**li"
# count = 0
# for item in a:
#     if not ("a"<=item<="z") and not ("A"<=item<="z") and not ("0"<=item<="9"):
#         count += 1
# print(count)

# a = ["google.txt", "amazon.com", "apple.com"]
# for item in a:
#     b = item.split(".")
#     if len(b[0])%2 == 0:
#         pass
#     else:
#         print(b[0])

# nums = [10, 20, 30, 40]
# num = 50
# for index, item in enumerate(nums):
#     if item == num:
#         print(f"{num} is present")
#         break
# else:
#     print("element is not pressent")

# s = "jekkdkjkio#4546y"
# a = 0
# for item in s:
#     if item.isalpha():
#         if item.lower() not in "aeiou":
#             print(item, end=" ")
#             a += 1

# a = "hello world"
# for item in range(len(a)):
#     print(item, a[item])

# a = "hello world"
# for index,item in enumerate(a):
#     print(index, item)

# a = "12@@$kffo#$mkrt4TR%^%#"
# for item in len(a):
    # if  not ("A"<=item<="Z" or "a"<=item<="z" or "0"<=item<="9"):
    #     print(item, end=" ")

# a = [1, 2, 3, 4, 5]
# b = 3
# for item in a:
#     if b == item:
#         continue
#
#     print(item)

# a = ["apple", "google", "apple", "yahoo", "google", 1, 2, 3, 3.3, 3+3j]
# for item in set(a):
#     print(item)

# for item in a:
#     if isinstance(item,(int,bool,float,complex)):
#         print(item, end=" ")

# d = {"a":1, "b":2, "c":3}
# for index, (key, value) in enumerate(d.items()):
#     print(index, key, value, end=" ", sep="-")


# def count_(func):
#     def wrapper(*args, **kwargs):
#         func(*args, **kwargs)
#         count = 0
#         for i in args:
#             count += 1
#         for j in kwargs:
#             count +=1
#         return count
#     return wrapper
#
# @count_
# def spam(*args, **kwargs):
#     return args,kwargs
# a = 2,3,4,4
# print(spam(a,12,34,c=3))



