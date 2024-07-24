
# This is no optimizable
# import sys
# n= int(sys.stdin.readline().strip())
# data = [sys.stdin.readline().strip() for _ in range(n)]

# distinct_words = set(data)
# print(len(distinct_words))

# for i in range(len(distinct_words)):
#     ocurrences = data.count(data[i])
#     print(ocurrences, end=' ')


from collections import OrderedDict

n = int(input().strip())
data = [input().strip() for _ in range(n)]

word_count = OrderedDict()
for word in data:
    if word not in word_count:
        word_count[word] = 0
    word_count[word] += 1

print(len(word_count))
print(*word_count.values())