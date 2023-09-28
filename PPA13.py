#ppa13.py
x = int(input())
cfrac = x

while True:
    
    term = int(input())
    
    if term == -1:
        break
    
    cfrac = 1 / (cfrac + term)

print (cfrac)
