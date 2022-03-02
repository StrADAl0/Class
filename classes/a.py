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
        self.n -= 2 * n
        self.draw()
        

    def show(self):
        for i in self.grid:
            t = i + i[len(self.grid) - 2::-1]
            print(*t, sep='')
        for i in self.grid[len(self.grid) - 2::-1]:
            t = i + i[len(self.grid) - 2::-1]
            print(*t, sep='')
    
    def freeze(self, n):
        for i in range(n):
            self.grid.insert(0, ['-'] * int(self.n / 2 + 1))
        for i in range(n):
            for j in self.grid:
                j.insert(0, '-')
        self.n += 2 * n
        self.draw()
    
    def thicken(self):
        t = 0
        for i in range(len(self.grid)):
            if self.grid[-1][i] == '*':
                t = i 
        ans = 0
        for i in range(len(self.grid)):
            if self.grid[i][t] != '*':
                ans = i
        for i in range(-1, -(ans + 1), -1):
            for j in range(t + 1, len(self.grid())):
                self.grid[i][j] = '*'
        

sf = SnowFlakes(29)
sf.thicken()
sf.show()