class Quadratic:
    def __init__(self, *koef):
        self.a, self.b, self.c = koef
        self.roots = Quadratic.root(*koef)
    
    @staticmethod
    def func(ans, a, b, c):
        return a * (ans ** 2) + b * ans + c

    @staticmethod
    def root(a, b, c):
        d = b ** 2 - 4 * a * c
        if d < 0:
            return None
        elif d == 0:
            ans = -b / (2 * a)
            return [ans, Quadratic.func(ans, a, b, c)]
        else:
            ans1 = (-b - d ** (1 / 2))/ (2 * a)
            ans2 = (-b + d ** (1 / 2))/ (2 * a)
            return [ans1, Quadratic.func(ans1, a, b, c), ans2, Quadratic.func(ans2, a, b, c)]

    def branch(self):
        if self.a > 0:
            return "up"
        else:
            return "down"

    def x_sect(self):
        if self.b ** 2 - 4 * self.a * self.c > 0:
            return 2
        elif self.b ** 2 - 4 * self.a * self.c == 0:
            return 1
        else:
            return 0
    
    def top(self):
        d = self.b ** 2 - 4 * self.a * self.c
        return ((-1 * self.b) / (2 * self.a), -1 * d / (4 * self.a))

    def y_sect(self):
        return (0, self.c)
    
    def sections(self):
        return self.roots
