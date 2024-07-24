import textwrap
import sys
string = sys.stdin.readline().strip()
max_width = int(sys.stdin.readline())


def wrap(string, max_width):
    return textwrap.fill(string, max_width)
result=wrap(string, max_width)
print(type(result))


# for i in range(0,len(string),number):
#     print(string[i:i+number])