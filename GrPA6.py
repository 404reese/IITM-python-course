#this should pass all public & pvt cases
M = int(input())
N = int(input())
k=0
if M < N:
    print(M)
else:
    M1=M-N
    if M1 < N:
        print(k)
    else:
        M2=M1-N
        k=k+1
        if M2 < N:
            print(k)
        else:
           M3=M2-N
           k=k+1
           if M3 < N:
              print(k)
           else:
               M4=M3-N
               k=k+1
           if M4 < N:
              print(k)
           else:
               M5=M4-N
               k=k+1
           if M5 < N:
              print(k)