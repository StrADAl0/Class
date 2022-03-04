class SnowFlakes:
    def __init__(self, side):
        self.side = side
        self.flake = []
        self.fill()

    def draw(self):
        self.flake = [['-'] * self.side for _ in range(self.side)]
        for i in range(self.side):
            for j in range(self.side):
                if i == j or j == self.side // 2 or \
                        i + j == self.side - 1 or i == self.side // 2:
                    self.flake[i][j] = '*'

    def show(self):
        print(*[''.join(row) for row in self.flake], sep='\n')

    def thaw(self, n):
        k = 0
        while k < n:
            for i in range(self.side):
                for j in range(self.side):
                    if i == k or j == k or i == self.side - k - 1 or j == self.side - k - 1:
                        self.flake[i][j] = '-'
            k += 1

    def freeze(self, n):
        self.side += 2 * n
        self.draw()

    def thicken(self):
        self.flake = [['-'] * self.side for _ in range(self.side)]
        for i in range(self.side):
            for j in range(self.side):
                if i == j or j == self.side // 2 or \
                        i + j == self.side - 1 or i == self.side // 2 or \
                        i == j + 1 or i == j - 1 or j == i + 1 or j == i - 1 or \
                        i + j == self.side or i + j == self.side - 2 or \
                        i == self.side // 2 + 1 or i == self.side // 2 - 1 or \
                        j == self.side // 2 + 1 or j == self.side // 2 - 1:
                    self.flake[i][j] = '*'