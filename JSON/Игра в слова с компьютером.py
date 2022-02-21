import json


haram = ['ъ', 'ь', 'ы']


with open('russian_words.json', encoding='utf8') as infile:
    data = json.load(infile)


used = []


game = True
last_letter = None


while game:
    while True:
        t = input()
        t = t.lower()
        if t == 'сдаюсь':
            print('Игра закончена! Победил компьютер.')
            game = False
            break
        if t[0] != last_letter:
            if last_letter is not None:
                print('Это слово не на букву {}.'.format(last_letter))
                continue
        if t not in data[last_letter]:
            print('Такого слова нет.')
            continue
        if t in used:
            print('Это слово уже было.')
            continue
        last_word = t
        break
    while last_word[-1] in haram:
        last_word = last_word[:len(last_word) - 1]
    last_letter = last_word[-1]
    for i in data[last_letter]:
        if i not in used:
            used.append(i)
            print(i)
            for j in range(len(i) - 1, -1, -1):
                if i[j] not in haram:
                    last_letter = i[j]
                    break
            break
        if i == data[last_letter][-1]:
            print('Игра закончена! Победил пользователь.')
            game = False
            break
    if not game:
        break
    if set(data[last_letter]) in set(filter(lambda x: x[0] == last_letter, used)):
        print('Игра закончена! Победил компьютер.')
        game = False
        break