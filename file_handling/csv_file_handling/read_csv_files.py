import csv
path = r'C:\Users\DELL\PycharmProjects\learning\files_directory\csv_files\employees.csv'

from collections import defaultdict


# with open(path) as csv_file:
#     read_obj = csv.reader(csv_file)
#     print(read_obj)
#     for row in read_obj:
#         print(row)


# with open(path) as csv_file:
#     read_obj = csv.DictReader(csv_file)
#     print(read_obj)
#     for row in read_obj:
#         print(row)


with open(path) as csv_file:
    r_obj = csv.reader(csv_file)
    dd = defaultdict(list)
    for row in r_obj:
        dd[row[2]] += [row[0]]
# print(dd)
"""wap to sort the shares in the test csv file based on the share prices"""
path1 = r"C:\Users\DELL\PycharmProjects\learning\files_directory\csv_files\test.csv"
# with open(path1) as file:
#     r_obj = csv.DictReader(file)
#     l = list(r_obj)
#     res = sorted(l, key=lambda d: float(d["price"]))
#     print(list(res))


# with open(path) as csv_file:
#     read_obj = csv.DictReader(csv_file)
#     print(read_obj)
#     for row in read_obj:
#         print(row)

"""wap to read all the names of the employee csv file"""
# with open(path) as file:
#     r_obj = csv.reader(file)
#     for row in r_obj:
#         print(row[0])

"""wap to print only the names with salaries greater than 70000"""
# with open(path) as file:
#     r_obj = csv.reader(file)
#     header = next(r_obj)
#     for row in r_obj:
#         if int(row[-1])>70000:
#             print(row[0])

with open(path) as file:
    r_obj = csv.reader(file)
    header = next(r_obj)
    d = defaultdict(list)
    for row in r_obj:
        d[row[1]] += [row[0]]
print(d)


















