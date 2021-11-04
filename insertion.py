import numpy as np
from matplotlib import pyplot as plt


def sort(arr):
    i = 1
    while i < len(arr):
        j = i
        while (j > 0) and (arr[j-1] > arr[j]):
            swap(arr, j-1, j)
            j -= 1
        i += 1


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    return arr

