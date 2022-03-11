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
        for i, j in zip(self.values[:len_s], self.values[len_s:]):
            if i is not None:
                ans.append(i)
            if j is not None:
                ans.append(j)
        self.values = ans
    
    def get_list(self):
        return self.values
