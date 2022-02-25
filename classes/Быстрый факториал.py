class QuickFactorial:
    def __init__(self):
        self.values = {0: 1, 1: 1}
    
    def result(self, n):
        for i in range(list(self.values.keys())[-1] + 1, n + 1):
            self.values[i] = self.values[list(self.values.keys())[-1]] * i
        return self.values[n]


q = QuickFactorial()
print(q.result(30))