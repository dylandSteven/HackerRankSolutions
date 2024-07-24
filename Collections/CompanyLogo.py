import sys
from collections import OrderedDict

text = sys.stdin.readline()
result={}

for i in text:
    if i in result:
        result[i]+=1
    else:
        result[i]=1
sorted_dict = dict(sorted(result.items(), key=lambda item: item[1],reverse=True))

for key in sorted_dict:
    if sorted_dict[key]!=1:
        print(key,sorted_dict[key])