import sys
import random
import time

sys.stdin = open('SORT.INP', 'r')
sys.stdout = open('MERGESORT.OUT', 'w')

def MergeSort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = MergeSort(arr[:mid])
    right = MergeSort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

nTEST = int(input())

for i in range(nTEST):
    n = int(input())
    arr = list(map(float, input().split()))

    start = time.perf_counter()

    arr = MergeSort(arr)
    
    end = time.perf_counter()
    
    print(round(end - start, 6))


