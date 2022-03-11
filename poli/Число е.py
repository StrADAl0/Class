class EulerNumber:
    def __init__(self, n):
        self.n = n
    
    @staticmethod
    def faq(n):
        ans = 1
        for i in range(1, n + 1):
            ans *= i
        return ans

    def get_number(self, x=1):
        ans = 0
        for i in range(self.n):
            ans += (x ** i) / EulerNumber.faq(i)
        return ans
