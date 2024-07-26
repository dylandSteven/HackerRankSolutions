import sys
word=sys.stdin.readline().strip()
second_word=sys.stdin.readline().strip()
def count_overlapping(main_string, sub_string):
    count = 0
    start = 0
    while start < len(main_string):
        pos = main_string.find(sub_string, start)
        if pos != -1:
            count += 1
            start = pos + 1
            print(start)
        else:
            break
    return count
print(count_overlapping(word,second_word))