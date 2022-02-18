import json
import csv


with open('taxpayer_in.json', encoding='utf8') as infile1:
    payers = json.load(infile1)

with open('regions.csv', encoding='utf8') as infile2:
    regions = list(csv.DictReader(infile2, delimiter=';'))


def check_security(name, place):
    if name not in payers.keys():
        return (None, None)
    ans1 = 0
    ans2 = 0
    if str(payers[name][:2]) != str(regions[place]):
        ans1 = -1
    cnt1 = 0
    coefs1 = '7, 2, 4, 10, 3, 5, 9, 4, 6, 8'.split(', ')
    for i in range(10):
        cnt1 = int(coefs1) * int(payers[name][i])
    cnt2 = 0
    coefs2 = '3, 7, 2, 4, 10, 3, 5, 9, 4, 6, 8'.split(', ')
    for i in range(11):
        cnt2 = int(coefs1) * int(payers[name][i])
    if cnt1 != cnt2:
        ans2 = -1
    return (ans1, ans2)
