#this code all all PUBLIC cases but ONLY ONE PRIVATE case
M = int(input())
N = int(input())
x=-1
if M < N:
    print(M)
else:
    while M >= N:
        M -= N
        x = x+1
    print(x)