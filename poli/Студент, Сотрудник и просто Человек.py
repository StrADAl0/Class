class Human:
    def __init__(self, name):
        self.name = name
    
    def get_name(self):
        return self.name


class Student:
    def __init__(self, name, university):
        self.name = name
        self.university = university
        self.year = 1
    
    def get_name(self):
        return self.name
    
    def get_university(self):
        return self.university
    
    def get_year(self):
        return self.year
    
    def study(self):
        self.year = min(6, self.year + 1)


class Employee:
    positions = ['junior', 'middle', 'senior', 'lead']

    def __init__(self, name, company):
        self.name = name
        self.company = company
        self.position = 0
        
    def get_name(self):
        return self.name
    
    def get_company(self):
        return self.company
    
    def work(self):
        self.position += 1
        self.position = min(3, self.position)
    
    def get_position(self):
        return self.positions[self.position]
