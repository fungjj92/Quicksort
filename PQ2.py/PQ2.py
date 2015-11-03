__author__ = 'jfung'

import numpy

# Save ints to array
list = []
intList = []
with open('test.txt', 'r') as f:
    list = f.read().splitlines()
    intList = [int(i) for i in list]
f.close()

count = 0

def quickSort(arr, count):
    if len(arr) < 2:
        return arr, count

    # only handles unique arrays
    def partition(array, count):
        n = len(array)
        location = 0
        pivotVal = array[0]
        for i in range(0, n):
            if pivotVal > array[i]:
                array.insert(0, array.pop(i))
                location += 1
            elif pivotVal < array[i]:
                array.insert(location + 1, array.pop(i))
            else:
                continue
        left = array[:location]
        right = array[location + 1:]
        count += len(left) + len(right) - 2
        return left, right, count

    left, right, count = partition(arr, count)
    quickSort(left, count)
    quickSort(right, count)

    return arr, count

A, C = quickSort(intList, count)
print A, C


