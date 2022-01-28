'''d = {"a" : 1, "b": 2, "c":3, "d":5}
for key in d:
    print(d[key], end=" ")
print()
for key, value in d.items():
    print(key, value, end = " ")'''

'''string = "hello world"
d ={}
for char in set(string):
    count = 0
    
    for j in string:
        if char==j:
            count+=1
    d[char] = count
print(d)'''

'''string = "hello world"
d= {}
for char in string:
    if char not in d:
        d[char] = 1
    else:
        d[char]+=1
print(d)'''
'''
s = "hai how are you, what are you"
d ={}
a = s.split(" ")
for char in a:
     d[char]=a.count(char)
print(d)

print("============")

s = "hai how are you, what are you"
d1 = {}
a = s.split(" ")
for word in a:
    if word not in a:
        d[word] = 1
    else:
        d[word] += 1
print(d)

print("======")

s = "hai how are you, what are you"
d3 = {}
a = s.split(" ")
for word in a:
    if len(word)%2==0:
        d3[word] = len(word)
print(d3)

print("========")

s = "hai how are uou, what are you"
d4 = {}
a = s.split(" ")
for word in a:
    if word[0] in "aeiouAEIOU":
        d4[word]=len(word)
print(d4)

print("=======")

s = "hai how are uou, what are you"
d5 = {}
a = s.split(" ")
for word in a:
    if a.count(word)>1:
        continue
    else:
        d5[word] = a.count(word)
print(d5)'''

'''s = "hello world welcomr to python programming hi there"
d ={}
a = s.split()
for word in a:
    if word[0] not in d:
        d[word[0]] = [word]
    else:
        d[word[0]]+=[word]
print(d)'''
'''
name = ["apple", "google", "gmail", "yahoo", "gmail", "apple", "gmail", "google"]
d ={}
for index,word in enumerate(name):
    if word not in d:
        d[word] = [index]
    else:
        d[word]+=[index]
print(d)'''

d = {"1": 'one', "2":'two', "3": 'three', "4": 'four'}
d1 = {}
for key in d:
    value = d[key]
    d1[value] = key
print(d1)






