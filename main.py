import numpy as np
from tracked_array import TrackedArray
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import quicksort as qs
import bubble as bs
import insertion as ins

plt.rcParams["figure.figsize"] = (12, 8)
plt.rcParams["font.size"] = 16


def plot(array, sorter):
    fig, ax = plt.subplots()
    ax.bar(np.arange(0, len(arr), 1), array, align="edge", width=0.8)
    ax.set(xlabel="Index", ylabel="Value", title=sorter)
    plt.show()


def random_arr(size):
    array = np.round(np.linspace(0, 1000, size), 0)
    np.random.shuffle(array)
    array = TrackedArray(array)
    return array

sorter = "Unsorted"
arr = random_arr(30)

sorter = "Insertion"
ins.sort(arr)

plot(arr, sorter)

##################################################################################

sorter = "Quick"
qs.sort(arr, 0, len(arr)-1)

plot(arr, sorter)

#####################################################

sorter = "Bubble"
bs.sort(arr)
plot(arr, sorter)
