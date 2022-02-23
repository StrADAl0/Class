class Quadratic:

    def __init__(self, *koef):
        self.a, self.b, self.c = koef
        self.roots = Quadratic.root(*koef)
    
    @staticmethod
    def check(x):
        return (abs(x), 1 if x < 0 else 0)

    @staticmethod
    def root(a, b, c):
        d = b * b - 4 * a * c
        if d < 0:
            return None
        x1 = (-b + d ** (1 / 2)) / (2 * a)
        x2 = (-b - d ** (1 / 2)) / (2 * a)
        y1 = a * x1 * x1 + b * x1 + c
        y2 = a * x2 * x2 + b * x2 + c
        num = 10 ** (-15)
        if abs(y1) < num:
            y1 = 0.0
        if abs(y2) < num:
            y2 = 0.0
        if d == 0:
            return x1, 0.0
        st = sorted([(x1, y1), (x2, y2)], key=lambda x: (Quadratic.check(x)))
        return *st[0], *st[1]

    def branch(self):
        return "up" if self.a > 0 else "down"

    def top(self):
        x = -self.b / (2 * self.a)
        y = self.a * x * x + self.b * x + self.c
        return x, y

    def y_sect(self):
        return 0, self.c

    def x_sect(self):
        return 0 if not self.roots else len(self.roots) // 2

    def sections(self):
        return self.roots

equation = Quadratic(1.6, 0, -3)
print(equation.branch())
print(equation.sections())
print(equation.x_sect())
print(equation.y_sect())