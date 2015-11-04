__author__ = 'jfung'

import numpy

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
        quickSort(arr, start, split)
        quickSort(arr, split + 1, end)


def partition(array, start, end):
    pivot = start
    #swap pivot element to start if not
    if pivot != start:
        array[pivot], array[start] = array[start], array[pivot]
    #update count
    length = len(array[start:end])
    set(length)
    i = start + 1
    pivotVal = array[start]
    for j in range(i, end):
        if array[j] < pivotVal:
            array[j], array[i] = array[i], array[j]
            i += 1
    array[start], array[i-1] = array[i-1], array[start]
    print "After: {} Pivot: {} ({})".format(array[start:end], pivot, array[pivot])
    print ""
    return i-1


quickSort(intList, 0, len(intList))
print globalCount
print intList
