import re
import sys

dem = sys.stdin.readline().split();
r = int(dem[0])
c = int(dem[1])
rows = [l for l in sys.stdin]
text = "";
for i in range(c):
    for j in range(r):
        text = text+rows[j][i]

print(re.sub(r"(?<=\w)\W+(?=\w)", " ", text))
