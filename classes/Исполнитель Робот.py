class Robot:
    def __init__(self, start):
        self.point = list(start)
        self.path1 = [start]
    
    def move(self, direct):
        for i in direct:
            if i == 'N':
                self.point = [self.point[0], self.point[1] + 1]
            elif i == 'S':
                self.point = [self.point[0], self.point[1] - 1]
            elif i == 'W':
                self.point = [self.point[0] - 1, self.point[1]]
            elif i == 'E':
                self.point = [self.point[0] + 1, self.point[1]]
            self.path1.append(tuple(self.point))
    
    def path(self):
        t = self.path1[:]
        self.path1.clear()
        return t