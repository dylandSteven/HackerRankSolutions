from functools import reduce
import sys
from decimal import Decimal, getcontext
from math import gcd
from fractions import Fraction

n = int(sys.stdin.readline().strip())

array = []
for _ in range(n):
    row = list(map(int, sys.stdin.readline().strip().split()))
    frac1 = Fraction(row[0], row[1])
    array.append(frac1)
    
reduceFraction = reduce(lambda x, y: x * y, array)
print(reduceFraction.numerator, reduceFraction.denominator)
