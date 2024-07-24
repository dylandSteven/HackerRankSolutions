import sys
import re
number= sys.stdin.readline().strip()
pattern = re.compile(r'^[\w|\-]+@[A-Za-z0-9]+\.[A-Za-z]{1,3}$')

filtered_emails =[]
for i in range(int(number)):
    email = sys.stdin.readline().strip()
    if email.find('@') != -1 and email.find('.') != -1:
        if email.find('@') < email.find('.') and pattern.match(email):
            filtered_emails.append(email)
        else:
            print("Invalid")
    else:
        print("Invalid")
        
        
filtered_emails.sort()
print(filtered_emails)