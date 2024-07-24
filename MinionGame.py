from collections import Counter

string  = "BANANA"
kevinArray = []
stuartArray = []
def kevin_total():
    if(string[0]!='A' and string[0]!='E' and string[0]!='I' and string[0]!='O' and string[0]!='U'):
        kevinArray.append(string[0])
    for i in range(1,len(string)):
        kevinArray.append(string[1:i+1])
    kevinArray.pop(0)    
    return kevinArray

def stuart_total():
    seen = set()
    vowels = 'AEIOU'
    for i in range(len(string)):
        if string[i] not in vowels:
            for j in range(i + 1, len(string) + 1):
                substring = string[i:j]
                if substring not in seen:
                    stuartArray.append(substring)
                    seen.add(substring)
    return seen


def count_overlapping(main_string, sub_string):
    count = 0
    start = 0
    while start < len(main_string):
        pos = main_string.find(sub_string, start)
        if pos != -1:
            count += 1
            start = pos + 1
        else:
            break
    return count


def count_kevin():
    kevin_vowels = 0
    for i in range(0,len(kevinArray)):
        count = count_overlapping(string,kevinArray[i])
        kevin_vowels += count
    return kevin_vowels


def count_stuart():
    stuart_consonants = 0
    for i in range(0,len(stuartArray)):
        count = count_overlapping(string,stuartArray[i])
        stuart_consonants += count
    return stuart_consonants

def main():
    kevin_total()
    stuart_total()
    kevin_count = count_kevin()
    stuart_count = count_stuart()
    if(kevin_count > stuart_count):
        print("Kevin",kevin_count)
    elif(stuart_count > kevin_count):
        print("Stuart",stuart_count)
    else:
        print("Draw")
    
main()