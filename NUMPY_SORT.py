import sys
import numpy as np
import time

sys.stdin = open('SORT.INP', 'r')
sys.stdout = open('NUMPYSORT.OUT', 'w')

nTEST = int(input())

for i in range(nTEST):
    n = int(input())
    arr = list(map(float, input().split()))

    start = time.perf_counter()

    arr = np.sort(arr)
    
    end = time.perf_counter()
    
    print(round(end - start, 6))

