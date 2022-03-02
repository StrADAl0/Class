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
        for i in range(int(self.n / 2) + 1):
            t = ['-'] * int(self.n / 2 + 1) 
            self.grid.append(t)

    def draw(self):
        for i in range(-1, -int(self.n / 2) - 2, -1):
            self.grid[i][i] = '*'
            self.grid[i][-1] = '*'
            self.grid[-1][i] = '*'
    
    def thaw(self, n):
        self.empty()
        self.n -= n
        self.draw()
        

    def show(self):
        for i in self.grid:
            t = i + i[len(self.grid) - 2::-1]
            print(*t, sep='')
        for i in self.grid[len(self.grid) - 2::-1]:
            t = i + i[len(self.grid) - 2::-1]
            print(*t, sep='')
    
    def freeze(self, n):
        self.n += n
        self.empty()
        self.draw()
    
    def thicken(self):
        for i in range(int(self.n / 2) - 1):
            self.grid[i][i + 1] = '*'
            self.grid[i + 1][i] = '*'
            self.grid[i][-2] = '*'
            self.grid[-2][i] = '*'
        


sf = SnowFlakes(15)
sf.thicken()
sf.show()