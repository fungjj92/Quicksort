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

## RETURNS SORTED LIST, INCORRECT COUNT ##

def quickSort(arr, length):
    if length < 2:
        return arr

    pivot = 0

    i = partition(arr, length, pivot)

    leftA = quickSort(arr[:i], len(arr[:i])-1)
    rightA = quickSort(arr[i:], len(arr[i:]))

    return leftA+rightA


def partition(array, length, pivot):
    #update count
    set(length)
    #swap pivot element to index 0, if pivot not 0
    if pivot != 0:
        array[pivot], array[0] = array[0], array[pivot]
    p = array[0]
    i = 1
    for j in range(i, length):
        if array[j] < p:
            array[j], array[i] = array[i], array[j]
            i += 1
    array[0], array[i-1] = array[i-1], array[0]
    return i

finalA = quickSort(intList, len(intList))
print globalCount
print finalA
