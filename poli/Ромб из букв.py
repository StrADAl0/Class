class LettersRhombus:
    def __init__(self, letter, empty=' '):
        self.matrix = []
        self.letter = letter
        for i in range(1 + 2 * (ord(letter) - ord('A'))):
            t = []
            for j in range(1 + 2 * (ord(letter) - ord('A'))):
                t.append(empty)
            self.matrix.append(t)
        self.fill()
    
    def fill(self):
        t = ord(self.letter) - ord('A')
        letter = 'A'
        i = 0
        while t >= 0:
            self.matrix[i][t] = letter
            self.matrix[i][len(self.matrix) - t - 1] = letter
            letter = chr(ord(letter) + 1)
            t -= 1
            i += 1
        t += 2
        letter = chr(ord(letter) - 2)
        while t <= 3:
            if i >= len(self.matrix):
                break
            self.matrix[i][t] = letter
            self.matrix[i][len(self.matrix) - t - 1] = letter
            letter = chr(ord(letter) - 1)
            t += 1
            i += 1
    
    def rows(self):
        return [''.join(i) for i in self.matrix]
    
    def cols(self):
        ans = []
        for i in range(len(self.matrix)):
            t = []
            for j in range(len(self.matrix)):
                t.append(self.matrix[j][i])
            ans.append(''.join(t))
        return ans


lines = LettersRhombus("C")
print(*lines.cols(), sep="\n")