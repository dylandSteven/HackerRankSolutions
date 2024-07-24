import sys

result=0
array = [int(line.strip()) for line in sys.stdin]
matrix = [(array[i], array[i+1]) for i in range(0, len(array), 2)]
for pair in matrix:
    result += pair[0] ** pair[1]
    
print(result)