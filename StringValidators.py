import sys
string=sys.stdin.readline()

def contains_digit(string):
    for char in string:
        if char.isdigit():
            return True
    return False

def contains_alphabet(string):
    for char in string:
        if char.isalpha():
            return True
    return False

def contains_alnum(string):
    for char in string:
        if char.isalnum():
            return True
    return False

def contains_lower(string):
    for char in string:
        if char.islower():
            return True
    return False

def contains_upper(string):
    for char in string:
        if char.isupper():
            return True
    return False

print(contains_alnum(string))
print(contains_alphabet(string))
print(contains_digit(string))
print(contains_lower(string))
print(contains_upper(string))

