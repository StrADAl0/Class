class BeeElephant:
    def __init__(self, bee, eleph):
        self.bee = bee
        self.eleph = eleph
    
    def fly(self):
        return self.bee >= self.eleph

    def trumpet(self):
        print('tu-tu-doo-doo!') if self.eleph >= self.bee else print('wzzzzz')
    
    def eat(self, meal, value):
        if meal == 'nectar':
            self.bee += value
        else:
            self.eleph += value
    
    def get_parts(self):
        return (self.bee, self.eleph)
