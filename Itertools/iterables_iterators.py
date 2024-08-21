# import sys
# import itertools
# n= int( sys.stdin.readline())
# lista= []
# result = 0

# class NumberPair:
#     def __init__(self, number_up, number_down):
#         self.number_up = number_up
#         self.number_down = number_down
    
#     def __str__(self):
#         return f"({self.number_up}, {self.number_down})"


# def generate_tuplas(n:int):
#     for i in range(1, n+1):
#         for j in range(1, n+1):
#             if i != j and i < j:
#                 # print((i, j))
#                 new =  NumberPair(i, j)
#                 lista.append(new)


# generate_tuplas(n)
# for pair in lista:
#     print(pair)
#     result += (pair.number_up/pair.number_down)
#     print(result)
# print(result)


import itertools
import sys
n = int(sys.stdin.readline())
letters = sys.stdin.readline().split()
k = int(sys.stdin.readline())

nb, tot = 0, 0
for t in itertools.combinations([i for i in range(n)], k):
    tot += 1
    for i in t:
        # print(i)
        if letters[i] == 'a':
            nb += 1
            break
print(round(nb / tot, 12))