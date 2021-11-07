
def sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1) :
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    return arr
