class ShoppingList:
    def __init__(self, *args):
        self.list = list(args)
    
    def append(self, value):
        self.list.append((value, False))
    
    def values(self):
        return self.list
    
    def check(self, value):
        for i in range(len(self.list)):
            if self.list[i][0] == value:
                self.list[i] = (value, True)
                break
    
    def checked_values(self):
        return list(filter(lambda x: x[1], self.list))
    
    def rest_values(self):
        return list(filter(lambda x: not x[1], self.list))


class TODOList:
    def __init__(self, *args):
        self.list = sorted(list(args), key=lambda x: x[1], reverse=True)
    
    def append(self, value, urgency):
        self.list.append((value, urgency, False))
        self.list = sorted(self.list, key=lambda x: x[1], reverse=True)
    
    def values(self):
        return self.list
    
    def check(self, value):
        for i in range(len(self.list)):
            if self.list[i][0] == value:
                self.list[i] = (self.list[i][0], self.list[i][1], True)
                break
    
    def checked_values(self):
        return list(filter(lambda x: x[2], self.list))
    
    def rest_values(self):
        return list(filter(lambda x: not x[2], self.list))


class Route:
    def __init__(self, *args):
        self.list = list(args)
    
    def append(self, value, time):
        if int(self.list[-1].split(':')[0]) < int(time.split(':')[0]):
            self.list.append((value, time, False))
        elif int(self.list[-1].split(':')[0]) == int(time.split(':')[0]):
            if int(self.list[-1].split(':')[1]) < int(time.split(':')[1]):
                self.list.append((value, time, False))
    
    def values(self):
        return self.list
    
    def check(self, value):
        for i in range(len(self.list)):
            if self.list[i][0] == value:
                self.list[i] = (self.list[i][0], self.list[i][1], True)
                break
    
    def checked_values(self):
        return list(filter(lambda x: x[2], self.list))
    
    def rest_values(self):
        return list(filter(lambda x: not x[2], self.list))
