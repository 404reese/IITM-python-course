#ppa13.py
x = int(input())
cfrac = x

while True:
    
    term = int(input("Enter the next term of the continued fraction (or -1 to stop): "))
    
    if term == -1:
        break
    
    cfrac = 1 / (cfrac + term)

print (cfrac)
