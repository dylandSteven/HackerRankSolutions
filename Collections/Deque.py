import sys
from collections import deque
n=int(sys.stdin.readline())
deque=deque()
for _ in range(n):
    item=sys.stdin.readline().split()
    if item[0]=='append':
        deque.append(int(item[1]))
    elif item[0]=='appendleft':
        deque.appendleft(int(item[1]))
    elif item[0]=='pop':
        deque.pop()
    elif item[0]=='popleft':
        deque.popleft()    
print(*deque)