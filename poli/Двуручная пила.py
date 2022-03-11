from itertools import zip_longest


class TwoHandedSawUp:
    def __init__(self, values):
        self.values = values
    
    def sawing(self):
        ans = []
        self.values.sort()
        len_s = int(len(self.values) / 2)
        for i, j in zip(self.values[:len_s], self.values[len_s:]):
            if i is not None:
                ans.append(i)
            if j is not None:
                ans.append(j)
        self.values = ans
    
    def get_list(self):
        return self.values


class TwoHandedSawDown:
    def __init__(self, values):
        self.values = values
    
    def sawing(self):
        ans = []
        self.values.sort(reverse=True)
        len_s = int(len(self.values) / 2)
        for i, j in zip_longest(self.values[:len_s], self.values[len_s:]):
            if i is not None:
                ans.append(i)
            if j is not None:
                ans.append(j)
        self.values = ans
    
    def get_list(self):
        return self.values


def print_hist(array):
    for i in array:
        print('*' * i)


arr = [8, 6, 1, 2, 7, 4, 5, 3, 9]
thsu = TwoHandedSawUp(arr)
thsu.sawing()
print(*thsu.get_list())
print_hist(thsu.get_list())

thsd = TwoHandedSawDown(arr)
thsd.sawing()
print(*thsd.get_list())
print_hist(thsd.get_list())