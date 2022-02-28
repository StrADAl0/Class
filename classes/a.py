class SnowFlakes:
    def __init__(self, n):
        self.n = n
        self.grid = []
        self.empty()
        self.draw()
    
    def __len__(self):
        return len(self.grid)

    def empty(self):
        self.grid = []
        for i in range(self.n):
            t = ['-'] * self.n
            self.grid.append(t)

    def draw(self):
        t = int(len(self) / 2)
        for i in range(int(self.n / 2) + 1):
            self.grid[t + i][t] = '*'
            self.grid[t - i][t] = '*'
            self.grid[t + i][t + i] = '*'
            self.grid[t + i][t - i] = '*'
            self.grid[t - i][t + i] = '*'
            self.grid[t - i][t - i] = '*'
            self.grid[t][t + i] = '*'
            self.grid[t][t - i] = '*'
    
    def thaw(self, n):
        self.n -= n
        self.draw()
    
    def
    
    def show(self):
        for i in self.grid:
            print(*i)


sf = SnowFlakes(9)
sf.draw()
sf.show()