def creators(star, planets=8, alive=True):
    ans = 'Система звезды {}.'.format(star)
    ans += '\nКоличество планет: {}.'.format(planets)
    ans += '\nЖизнь есть!' if alive else '\nЖизни нет.'
    return ans
