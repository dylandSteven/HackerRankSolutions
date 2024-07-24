import sys
# input = int(sys.stdin.readline())
# for i in range(1, input):
#     print(i*(10**i-1)//9)

[print(i*(10**i-1)//9) for i in range(1, int(sys.stdin.readline()))]
