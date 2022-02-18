import json
import random

n = int(input())
with open('words.json', encoding='utf8') as infile:
    word = random.choice(json.load(infile)[n])


game = True
cipher = '*' * n
print('Your word {}. Enter the letter.'.format(cipher))
while game:
    letter = input()
    if not letter.isalpha():
        print('Bad input. Try once more, please.')
        continue
    if letter not in word:
        print('Your word {}. Enter the letter.'.format(cipher))
        continue
    for i in range(n):
        if word[i] == letter:
            cipher = cipher[:i] + letter + cipher[i + 1:]



