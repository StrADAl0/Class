class Talking:
    def __init__(self, name):
        self.name = name
        self.yes = 0
        self.no = 0
        self.stage = 1

    def to_answer(self):
        if self.stage:
            self.stage = 0
            self.yes += 1
            return 'moore-moore'
        else:
            self.stage = 1
            self.no += 1
            return 'meow-meow'
    
    def number_yes(self):
        return self.yes
    
    def number_no(self):
        return self.no
