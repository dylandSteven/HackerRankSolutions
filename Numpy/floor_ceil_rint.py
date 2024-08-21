import numpy
import sys
numpy.set_printoptions(sign=' ')

n= sys.stdin.readline().split()
n= numpy.array(n, float)
print(numpy.floor(n))
print (numpy.ceil(n))           
print (numpy.rint(n))