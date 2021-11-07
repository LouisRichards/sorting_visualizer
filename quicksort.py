def sort(arr, lo, hi):
    if lo < hi:
        part = partition(arr, lo, hi)
        sort(arr, lo, part - 1)
        sort(arr, part+1, hi)


def partition(arr, lo, hi):
    pivot = arr[hi]
    i = lo
    for j in range(lo, hi):
        if arr[j] < pivot:
            swap(arr, i, j)
            i += 1
    swap(arr, i, hi)
    return i


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    return arr
