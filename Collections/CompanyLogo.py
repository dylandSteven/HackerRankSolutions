# import sys
# from collections import OrderedDict

# text = sys.stdin.readline()
# result={}

# for i in text:
#     if i in result:
#         result[i]+=1
#     else:
#         result[i]=1
# sorted_dict = dict(sorted(result.items(), key=lambda item: item[1],reverse=True))
# for i in range(3):
#     print(list(sorted_dict.keys())[i],list(sorted_dict.values())[i])

import collections

s = sorted(input().strip())
s_counter = collections.Counter(s).most_common()
# print(s_counter)
# s_counter = sorted(s_counter, key=lambda x: (x[1] * -1, x[0]))
print(s_counter)
for i in range(0, 3):
    print(s_counter[i][0], s_counter[i][1])