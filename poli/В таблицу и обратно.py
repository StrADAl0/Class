class TableToLine:
    def __init__(self, matrix):
        self.matrix = matrix
    
    def resize(self):
        ans = []
        for i in self.matrix:
            ans += i
        return ans, len(self.matrix), len(self.matrix[0])


class LineToTable:
    def __init__(self, line, n, m):
        self.arr = line
        self.n, self.m = n, m
    
    def resize(self):
        ans = []
        for i in range(self.n):
            ans.append(self.arr[:self.m])
            self.arr = self.arr[self.m:]
        return ans, self.n, self.m
