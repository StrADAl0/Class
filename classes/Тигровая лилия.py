class TigerLily:
    def __init__(self, talk):
        self.themes = list(talk)
    
    def reverse_order(self):
        self.themes.reverse()
    
    def add_theme(self, value):
        self.themes.append(value)
    
    def shift_one(self):
        self.themes = self.themes[1:] + self.themes[0]
    
    def get_themes(self):
        return tuple(self.themes)
    
    def get_first(self):
        return self.themes[0]