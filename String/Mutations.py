import sys
word=sys.stdin.readline().strip()
position,character=sys.stdin.readline().strip().split()
print(word[:int(position)]+character+word[int(position)+1:])