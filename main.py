import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import quicksort as qs
import insertion as ins

plt.rcParams["figure.figsize"] = (12, 8)
plt.rcParams["font.size"] = 16


def plot(array):
    fig, ax = plt.subplots()
    ax.bar(np.arange(0, len(arr), 1), array, align="edge", width=0.8)

    plt.show()


def random_arr(size):
    array = np.round(np.linspace(0, 1000, size), 0)
    np.random.shuffle(array)
    return array


arr = random_arr(100)
plot(arr)

sorter = "Insertion"
ins.sort(arr)

plot(arr)

##################################################################################

sorter = "Quick"
qs.sort(arr, 0, len(arr)-1)

plot(arr)

