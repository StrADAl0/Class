class Avalanche:
    def __init__(self):
        self.string = 'O'
    
    def go(self):
        print(self.string)
        t = ''
        for i in self.string:
            if i == 'o':
                t += 'oOo'
            else:
                t += 'ooOoo'
