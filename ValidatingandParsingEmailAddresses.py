import sys
import email.utils
import re
number = int(sys.stdin.readline())
array = [sys.stdin.readline().rstrip() for _ in range(number)]

def validate_email(email):
    pat = r'^[a-zA-Z][\w.-]+@[a-z]+\.[a-z]{1,3}$'    
    if(re.match(pat, email)):
        return True
    else:
        return False

for i in array:
    pairEmail= email.utils.parseaddr(i)
    if(validate_email(pairEmail[1])):
        print(email.utils.formataddr((pairEmail[0], pairEmail[1])))
    