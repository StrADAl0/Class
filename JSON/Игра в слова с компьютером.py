import json


haram = ['ъ', 'ь', 'ы']

with open('russian_words.json', encoding='utf8') as infile:
    data = json.load(infile)


used = []

last_word = input().lower()
game = True
while game:
    if last_word.lower() == 'сдаюсь':
        print('Игра закончена! Победил компьютер.')
        game = False
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
        if i == data[last_letter][-1]:
            print('Игра закончена! Победил пользователь.')
            game = False
            break
    if set(filter(lambda x: x[0] == last_letter, used)) == set(data[last_letter]):
        print('Игра закончена! Победил компьютер.')
        game = False
        break
    while True:
        last_word = input().lower()
        if last_word.lower() == 'сдаюсь':
            print('Игра закончена! Победил компьютер.')
            game = False
            break
        if last_word[-1] != last_letter:
            print('Это слово не на букву {}.'.format(last_letter))
            continue
        if last_word not in data[last_letter]:
            print('Такого слова нет.')
            continue
        if last_word in used:
            print('Это слово уже было.')
            continue
