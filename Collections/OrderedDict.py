import sys
result = {}

def read_input():
    num_students = int(sys.stdin.readline().strip()) 
    for _ in range(num_students):
        data = sys.stdin.readline()
        parts = data.rsplit(' ', 1)
        key = parts[0]
        value = int(parts[1])
        if key in result:
            result[key] += value
        else:
            result[key] = value
read_input()

for key, value in result.items():
    print(f"{key} {value}")
