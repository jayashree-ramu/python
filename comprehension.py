'''
a = ['python',10,3.4, 'selenium','java']
b = []
for i in enumerate(a):
    b.append(i)
print(b)

# using comprehension
a = ['python',10,3.4, 'selenium','java']
b = [item for item in enumerate(a)]
print(b)

""" create list of even number"""
a = list(range(10))
even = []
for item in a:
    if item%2 == 0:
        even.append(item)
print(even)'''


"""list with string starting with vowels"""
'''list = ["amazon","wallnut","you", "hello", "idea"]
a = []
for item in list:
    if item[0].lower() in "aeiou":
         a.append(item)
print(a)

b = [item for item in list if item[0].lower() in "aeiou"]
print(b)'''

'''
#set comprohension

a = ["amazon", "flipkart", "walmart", "gmail", "yahoo"]
b = set()
for index in a:
    b.add((index,len(index)))
print(b)

set = {(item,len(item)) for item in a}
print(set)

a = "JAYashreeDGT"
count1 = 0
count2 = 0
for item in a:
    if "a"<=item<="z":
        count1+=1
    elif "A"<=item<="Z":
        count2+=1
print(count1)
print(count2) '''