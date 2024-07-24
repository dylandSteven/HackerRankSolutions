
# Mi version
# import sys
# import re
# number= sys.stdin.readline().strip()
# number= int(number)+1
# ids= []
# marks= []
# name= []
# classs=[]
# def fill_list():
#     for _ in range(int(number)):
#         data= sys.stdin.readline().strip().split()
#         ids.append(data[0])
#         name.append(data[1])
#         marks.append(data[2])
#         classs.append(data[3])
        
# def select_list(ids,name,marks,classs):
#     for _ in range(4):
#         if ids[0]=='MARKS':
#             return ids
#         if marks[0]=='MARKS':
#             return marks
#         if name[0]=='MARKS':
#             return name
            
#         if classs[0]=='MARKS':
#             return classs

# def average_marks(marks):
#     total=0
#     for i in range(0,len(marks)):
#         total+=int(marks[i])
#     return total/len(marks)

# fill_list()

# result= select_list(ids,name,marks,classs)
# result.pop(0)

# int_arr = [int(re.sub(r'\D', '', elem)) for elem in result]
# print(average_marks(result))

################################################################################


import sys
import re

def read_input():
    num_students = int(sys.stdin.readline().strip()) + 1
    data = [sys.stdin.readline().strip().split() for _ in range(num_students)]
    return data

def select_column(data, column_name):
    column_index = next((i for i, col in enumerate(data[0]) if col == column_name), None)
    if column_index is None:
        return None
    return [row[column_index] for row in data]
        
def average_marks(marks):
    total = 0
    for i in range(1, len(marks)):
        total += int(marks[i])
    return total / (len(marks)-1)
data = read_input()
marks_column = select_column(data, 'MARKS')
print(average_marks(marks_column))
