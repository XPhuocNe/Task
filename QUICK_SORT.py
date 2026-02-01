import sys
import random
import time

sys.stdin = open('SORT.INP', 'r')
sys.stdout = open('QUICKSORT.OUT', 'w')

def QuickSort(arr):
    if (len(arr) <= 1):
        return arr
    
    pivot = random.choice(arr)
    
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return QuickSort(left) + middle + QuickSort(right)

nTEST = int(input())

for i in range(nTEST):
    n = int(input())
    arr = list(map(float, input().split()))

    start = time.perf_counter()

    arr = QuickSort(arr)
    
    end = time.perf_counter()
    
    print(round(end - start, 6))

