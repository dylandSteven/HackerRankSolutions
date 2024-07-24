import re
import sys
number = int(sys.stdin.readline())
array = [sys.stdin.readline().rstrip() for _ in range(number)]
def check_number(number):
    if is_valid_number(number)==True:
        if re.compile(r'[789]\d{9}').match(number):
            return "YES"
        else:
            return "NO"
    else:
        return "NO"        
        
    
def is_valid_number(number):
    if number.isdigit() and len(number) == 10:
        return True
    else:
        return False
    
for i in array:
    print(check_number(str(i)))