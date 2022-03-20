"""s = "hello world"
count = 0
for item in s:
    if item not in "aeiouAEIOU":
        print(item, end=" ")
        count+=1
print(count)"""

# """s = "hello world$%##$%12^&"
# for item in s:
#     if not ('0'<=item<='9') and not ('a'<=item<='z') and not  ('A'<=item<='Z'):
#         print(item)"""
# a = "hello world"
# for item in a:
#     if item in a:
#         print(a)


"""accessing class variable & modifying it without @class method"""
class my_name:
    company_name = "test yantra"
    def __init__(self,name, salary):
        self.name = name
        self.salary = salary

    def displya(self):
        print(self.name)
        print(self.salary)


emp1 = my_name("kashi", 50000)
# emp1.displya()
# my_name.displya(emp1)

"""accessing class variable using class name"""
# print(my_name.company_name)
"""accessing class variable using obkject"""
# print(emp1.company_name)
"""modifying class variable using object --->(it will modified in object only)"""

emp1.company_name = "tyss"
"""checking whether it was modified in class variable or not"""
# print(my_name.company_name)
"""checking whether it was modified in object or not"""
# print(emp1.company_name)


"""accessing class varible & modifying it uisng object with help of @classmethod"""
class my_name:
    company_name = "test yantra"
    def __init__(self,name, salary):
        self.name = name
        self.salary = salary


    def displya(self):
        print(self.name)
        print(self.salary)

    @classmethod
    def change_company(cls, new_name):
        cls.company_name = new_name



s1 = my_name("kashi", 50000)
# s1.displya()
# my_name.displya(emp2)
"""calling class method"""
# s1.change_company("test yanthra software solution")

"""accessing class variable using class name"""
# print(my_name.company_name)

"""accessing class variable using obkject"""
# print(s1.company_name)



# emp1.location_('bangalore')
#
# my_name.location_("india")


"""@staticmethod"""
class my_name:
    company_name = "test yantra"
    def __init__(self,name, salary):
        self.name = name
        self.salary = salary

    def displya(self):
        print(self.name)
        print(self.salary)

    @staticmethod
    def location_(location):
        print(f"employee location is:{location}")



a1 = my_name("kashi", 50000)
a1.displya()
a1.location_("bangalore")


