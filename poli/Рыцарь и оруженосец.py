class Knight:
    def __init__(self, name, *args):
        self.name = name
        self.weapons = args
    
    def info(self):
        return 'Knight({})'.format(self.name)
    
    def announce(self, lady):
        return 'Long live the noblest {}!'.format(lady)
    
    def fight(self, weapon):
        ans = ''
        if weapon not in self.weapons:
            return None
        for i in weapon.upper():
            ans += i if i not in 'aoeiuy'.upper() else ''
        return ans


class Squire:
    def __init__(self, name, knight, *args):
        self.name = name
        self.knight = knight
        self.weapons = args
    
    def info(self):
        return 'Squire({})'.format(self.name)
    
    def praise(self):
        return 'Glory to {}!'.format(self.knight)
    
    def fight(self, weapon):
        ans = ''
        if weapon not in self.weapons:
            return None
        for i in weapon.lower():
            ans += i if i not in 'aoeiuy' else ''
        return ans

kn = Knight("Lancelot", "sword", "spear", "mace", "dirk")
sq = Squire("Jhonny", "Lancelot", "stick")
for item in (kn, sq):
    print(item.info())
    print(item.fight("sword"))
    print(item.fight("stick"))
    if isinstance(item, Knight):
        print(item.announce("Izabella"))
    else:
        print(item.praise())