# import sys

# n = sys.stdin.readline().strip()
# list_tupla = []
# char = n[0]
# count = 0

# for i in range(len(n)):
#     if char == n[i]:
#         count += 1
#     else:
#         list_tupla.append((count, int(char)))
#         char = n[i]
#         count = 1

# # Add the last group
# list_tupla.append((count, int(char)))

# print(list_tupla)
import sys
from itertools import groupby

def compress_string(s):
    return [(len(list(group)), int(key)) for key, group in groupby(s)]

n = sys.stdin.readline().strip()
result = compress_string(n)
print(*result)

