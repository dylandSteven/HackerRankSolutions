import re
import sys
stringS=sys.stdin.readline().strip()
stringK=sys.stdin.readline().strip()
pattern = re.compile(stringK)
r = pattern.search(stringS)
if not r: print('(-1, -1)')
while r:
    print('({0}, {1})'.format(r.start(), r.end()-1))
    r = pattern.search(stringS, r.start()+1)
    
    

