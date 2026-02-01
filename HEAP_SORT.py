import sys
import random
import time

sys.stdin = open('SORT.INP', 'r')
sys.stdout = open('HEAPSORT.OUT', 'w')

import sys

def heapify(arr, n, i):
    
    largest = i
    l = 2 * i + 1 
    r = 2 * i + 2 

    if l < n and arr[l] > arr[largest]:
        largest = l

    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def HeapSort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    
    return arr

nTEST = int(input())

for i in range(nTEST):
    n = int(input())
    arr = list(map(float, input().split()))

    start = time.perf_counter()

    arr = HeapSort(arr)
    
    end = time.perf_counter()
    
    print(round(end - start, 6))

