class RPN:
    priority = {"*": 3, "/": 3, "+": 2, "-": 2, ")": 1, "(": 0}

    def __init__(self, prob):
        self.prob = prob.split()
        if self.check():
            self.sol = self.postfix()
        else:
            self.sol = self.prob
    
    def check(self):
        for i in range(1, len(self.prob)):
            if self.prob[i].isdigit() and self.prob[i - 1].isdigit():
                return 1
        return 0
    
    def postfix(self):
        if not self.check():
            return self.prob
        res = []
        stack = []
        expr = self.expr.split()
        for symb in expr:
            if symb.isdigit():
                res.append(symb)
            elif symb == "(":
                stack.append(symb)
            elif symb == ")":
                while stack[-1] != "(":
                    res.append(stack.pop())
                stack.pop()
            else:
                if not stack or self.priority[stack[-1]] < self.priority[symb]:
                    stack.append(symb)
                else:
                    while stack and self.priority[stack[-1]] >= self.priority[symb]:
                        res.append(stack.pop())
                    stack.append(symb)
        while stack:
            res.append(stack.pop())
        return ' '.join(res)

    def calculate(self):
        stack = []
        for i in self.prob.split():
            if i.isdigit():
                stack.append(float(i))
            else:
                t = stack.pop()
                if i == '+':
                    stack.append(stack.pop() + t)
                if i == '-':
                    stack.append(stack.pop() - t)
                if i == '*':
                    stack.append(stack.pop() * t)
                if i == '/':
                    stack.append(stack.pop() / t)
        return stack[-1]
