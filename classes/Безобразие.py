class BlackCat:
    def __init__(self, name):
        self.name = name
        self.wool = 0
        self.tail = 0
    
    def play(self, game, time):
        if game == 'wool':
            self.wool += time
        elif game == 'tail':
            self.tail += time
        else:
            self.wool, self.tail = 0, 0
        
    def get_play(self):
        return (self.wool, self.tail)
