class ChemicalPowerSource:
    def __init__(self, *args):
        self.content = args
    
    def get_content(self):
        return self.content
    
    def change_content(self, *args):
        self.content = args
    
    def voltage(self):
        return sum(list(map(len, self.content))) / 10
    

class MechanicalPowerSource:
    def __init__(self, *args):
        self.content = args
    
    def get_content(self):
        return self.content
    
    def change_content(self, *args):
        self.content = args
    
    def voltage(self):
        return sum(self.content) / 10


class BotanicPowerSource:
    def __init__(self, *args):
        self.content = args
    
    def get_content(self):
        return self.content
    
    def change_content(self, *args):
        self.content = args
    
    def voltage(self):
        return sum(list(map(len, self.content))) / 10