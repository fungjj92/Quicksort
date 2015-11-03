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

def quickSort(arr):
    if len(arr) < 2:
        return arr
    #set pivot to last element of array
    pivot = len(arr)-1
    i = partition(arr, pivot)

    quickSort(arr[:i])
    quickSort(arr[i+1:])

    return arr


def partition(array, pivot):
    n = len(array)
    set(n)
    p = array[pivot]
    i = pivot - 1
    for j in range(pivot, -1, -1):
        if array[j] > p:
            temp = array[j]
            array[j] = array[i]
            array[i] = temp
            i -= 1
    temp = array[i+1]
    array[i+1] = p
    array[pivot] = temp
    return i+1

quickSort(intList)
print globalCount
