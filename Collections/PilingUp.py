import sys
n= sys.stdin.readline()
matrix= []
for i in range(int(n)):
    m= sys.stdin.readline()
    matrix.append(list(map(int, sys.stdin.readline().split())))


def can_arrange_cubess(cubes):
    n = int(len(cubes))
    for _ in range(n):
        if cubes[0] >= cubes[len(cubes)-1]:
            a = cubes[0]
            cubes.pop(0)
        elif cubes[0] < cubes[len(cubes)-1]:
            a = cubes[len(cubes)-1]
            cubes.pop(len(cubes)-1)
        else:
            pass

        if len(cubes) == 1:
            return True

        if((cubes[0] > a) or (cubes[len(cubes)-1] > a)):
            return False
            break
            

for i in matrix:
    if can_arrange_cubess(i):
        print("Yes")
    else:
        print("No")