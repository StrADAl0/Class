def creators(name, planets=8, alive=True):
    ans = 'Система звезды ' + name + '.' + '\n'
    ans += 'Количество планет: ' + str(planets) + '.' + '\n'
    if(alive):
        ans += 'Жизнь есть!'
    else:
        ans += 'Жизни нет.'
    return ans


print(creators('Бетельгейзе', 3, False))