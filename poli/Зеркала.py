class RightMirror:
    def __init__(self, matrix):
        self.matrix = matrix
    
    def reflect(self):
        self.matrix = [i[::-1] for i in self.matrix]
    

class BottomMirror:
    def __init__(self, matrix):
        self.matrix = matrix
    
    def reflect(self):
        self.matrix = self.matrix[::-1]