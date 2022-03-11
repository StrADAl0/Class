class TypeStatistics:
    def __init__(self, *args):
        self.values = args
        self.dict = self.fill()
    
    def fill(self):
        ans = {}
        for i in self.values:
            ans.setdefault(i.__class__.__name__, [])
            ans[i.__class__.__name__].append(i)
        return ans
    
    def type_values(self):
        return self.dict
    
    def type_count(self):
        return len(self.dict.keys())
