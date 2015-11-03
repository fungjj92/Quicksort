__author__ = 'jfung'

import numpy
import statistics

# Save ints to array
list = []
intList = []
with open('test.txt', 'r') as f:
    list = f.read().splitlines()
    intList = [int(c) for c in list]
f.close()

def set(x):
    global globalCount
    globalCount += (x-1)

globalCount = 0

def quickSort(arr, start, end):
    if start < end:
        split = partition(arr, start, end)
        #recurse around sorted pivot
        quickSort(arr, start, split - 1)
        quickSort(arr, split + 1, end)


def partition(array, start, end):
    pivot = start
    #swap pivot element to start if not
    if pivot != start:
        array[pivot], array[start] = array[start], array[pivot]
    #update count
    length = len(array[start:end])
    set(length)
    pivotVal = array[start]
    i = start + 1
    for j in range(i, end):
        if array[j] < pivotVal:
            array[j], array[i] = array[i], array[j]
            i += 1
    array[start], array[i-1] = array[i-1], array[start]
    return i-1




def findMedian(arr):
    medianArray = [arr[0], arr[len(arr)//2 - 1], arr[len(arr)-1]]
    median = statistics.median(medianArray)
    if median == arr[0]:
        pivot = 0
    elif median == arr[len(arr)-1]:
        pivot = len(arr)-1
    else:
        pivot = len(arr)//2 - 1
    return pivot
#will need to replace pivot = ... -->> findMedian(array[start:end])

quickSort(intList, 0, len(intList))
print globalCount
print intList
