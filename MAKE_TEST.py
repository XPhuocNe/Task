import random 
import sys
import numpy

sys.stdout = open('SORT.INP', 'w')

nTEST = 10
print(nTEST)

for i in range(1):
    n = int(1e6)
    print(n)
    
    arr = [random.randint(1, 10**9) for _ in range(n)]

    arr.sort()
    
    for x in arr: 
        print(x, end = ' ')
    
    print('')
    
for i in range(1):
    n = int(1e6)
    print(n)
    
    arr = [random.randint(1, 10**9) for _ in range(n)]

    arr.sort(reverse=1)
    
    for x in arr: 
        print(x, end = ' ')
    
    print('')
    
for i in range(3):
    n = int(1e6)
    print(n)
    
    arr = [random.randint(1, 10**9) for _ in range(n)]
    
    for x in arr: 
        print(x, end = ' ')
    
    print('')
    
for i in range(5):
    n = int(1e6)
    print(n)
    
    arr = [round(random.uniform(0, 10**9), 2) for _ in range(n)]
    
    for x in arr: 
        print(x, end = ' ')
    
    print('')
    
        
        
        



