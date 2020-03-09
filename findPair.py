def findPair(array, x):
    left = 0
    right = len(array) - 1
    array.sort() # Python używa algorytmu Timsort, ale normalnie użyjemy MergeSort(array) pisząc to na tablicy
    while left < right :
        if array[left] + array[right] == x : return True
        elif array[left] + array[right] < x : left = left + 1
        else: right = right - 1
    return False
