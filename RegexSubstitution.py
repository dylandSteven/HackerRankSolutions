N = int(input())

for i in range(N):
    S = input()
    for i in range(3): #lazy
        S = S.replace(" || "," or ").replace(" && ", " and ")
    print (S)