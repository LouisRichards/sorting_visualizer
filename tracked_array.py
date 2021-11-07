import numpy as np

class TrackedArray():

    def __init__(self, arr):
        self.arr = np.copy(arr)
        self.reset()

    def reset(self):
        self.indicies = []
        self.values = []
        self.access_type = []
        self.full_copies = []

    def track(self, key, access_type):
        self.indicies.append(key)
        self.values.append(self.arr[key])
        self.access_type.append(access_type)
        self.full_copies.append(np.copy(self.arr))

    def GetActivity(self, idx=None):
        if isinstance(idx, type(None)):
            return [(i, op) for (i, op) in zip(self.indicies, self.access_type)]
        else:
            return (self.indicies[idx], self.access_type[idc])

    def __getitem__(self, key):
        self.track(key, "get")
        return self.arr.__getitem__(key)

    def __setitem__(self, key, value):
        self.arr.__setitem__(key, value)
        self.track(key, "set")

    def __len__(self):
        return self.arr.__len__()
