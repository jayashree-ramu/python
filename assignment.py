# # # a = "hello world"
# # # # print(a[::-1]) or
# # # for item in reversed(a):
# # #     print(item, end=" ")
# # # print()
# # # for index in range(-1,-len(a)-1,-1):
# # #     print(a[index], end="")
# # """ print tuple of character and itd ascii value by string"""
# # a = "hello world"
# # for item in a:
# #     print((item, ord(item)), end="")
#
# l = ["python", 1, 2, 3.3, 3+4j, (1,2,3)]
# l1 = []
# for item in l:
#     if isinstance(item, int):
#         l1.append(item)
# print(l1)
# """print integer ithe given list"""
# l = ["python", 1, 2, 3.3, 3+4j, (1,2,3)]
# for item in l:
#     if isinstance(item, int):
#         print(item , end=" ")

""" print even string and its length if length is odd reverse and print"""
# l = ["python", 1, 2, 3.3, 3+4j, (1,2,3), "hello world", "jayu"]
# for item in l:
#     if isinstance(item, str):
#         if len(item)%2==0:
#             print([item, len(item)], end=" ")
#         else:
#             print([item[::-1], len(item)])
'''
# l = ["python", 1, 2, 3.3, 3 + 4j, (1, 2, 3), "hello world", "jayu"]
# l1 = []
# for item in l:
#     if isinstance(item, str):
#         l1.append(item[::-1])
#     else:
#         l1.append(item)
# print(l1) or

l = ["python", 1, 2, 3.3, 3 + 4j, (1, 2, 3), "hello world", "jayu"]
for item in l:
    if isinstance(item, str):
        print(item[::-1], end=" ")
    else:
        print(item)'''

""" print extension in the list"""
"""a = ["google.com", "python.txt", "hello.world"]
for item in a:
    b = item.split(".")
    print(b[1])"""

