import json

#Запрещенные символы
haram = ['ъ', 'ь', 'ы']


#Чтение файла
with open('russian_words.json', encoding='utf8') as infile:
    data = json.load(infile)


#Использованные слова
used = []


#Начало игры
game = True

#Игра
while game:
    while True:
        #Вводится слово
        t = input()
        t = t.lower()
        #Проверка выхода из игры
        if t == 'сдаюсь':
            print('Игра закончена! Победил компьютер.')
            game = False
            break
        #Проверка правильной последней буквы
        if t[0] != last_letter:
            print('Это слово не на букву {}.'.format(last_letter))
            continue
        #Проверка существования слова
        if t not in data[last_letter]:
            print('Такого слова нет.')
            continue
        #Проверка, было ли использовано слово
        if t in used:
            print('Это слово уже было.')
            continue
        last_word = t
        break

    #Проверка последней буквы. Находим букву на которую начинаем новое слово
    while last_word[-1] in haram:
        last_word = last_word[:len(last_word) - 1]
    last_letter = last_word[-1]

    #Находим слово для ответа
    for i in data[last_letter]:
        #Если находим неиспользованное слово, то используем его
        if i not in used:
            used.append(i)
            print(i)
            #Проверка последней буквы слова компьютера
            for j in range(len(i) - 1, -1, -1):
                if i[j] not in haram:
                    last_letter = i[j]
                    break
            break
        #Условие для поражения компьютера
        if i == data[last_letter][-1]:
            print('Игра закончена! Победил пользователь.')
            game = False
            break
    #Проверка условия выхода
    if not game:
        break
    #Проверка условия поражения игрока
    if set(data[last_letter]) in set(filter(lambda x: x[0] == last_letter, used)):
        print('Игра закончена! Победил компьютер.')
        game = False
        break