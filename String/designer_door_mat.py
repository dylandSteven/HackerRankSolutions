import sys
n,m= map(int,sys.stdin.readline().split())
pattern='.|.'


def print_first_half(n,m):
    number = n//2
    for i in reversed(range(number)):
        print('-'*3*(i+1)+(pattern*((number-i)+(number-i-1)))+'-'*3*(i+1))
    print('WELCOME'.center(m,'-'))
    for i in range(number):
        print('-'*3*(i+1)+(pattern*((number-i)+(number-i-1)))+'-'*3*(i+1))

print_first_half(n,m)