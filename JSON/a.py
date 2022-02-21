import json
import csv


def check_security(name, place):
    with open('taxpayer_in.json', encoding='utf8') as infile1:
        payers = json.load(infile1)
    with open('regions.csv', encoding='utf8') as infile2:
        regions = list(csv.DictReader(infile2, delimiter=';'))

    p = list(filter(lambda x: (x['lastname'] == name[0], x['firstname'] == name[1], x['middlename'] == name[2]), payers))
    if len(p) == 0:
        return (None, None)
    p = p[0]
    ans1 = 0
    ans2 = 0
    if str(p['tin'][:2]) != str(list(filter(lambda x: x['region_name'] == place, regions))[0]['region_code']):
        ans1 = -1
    cnt1 = 0
    coefs1 = '7, 2, 4, 10, 3, 5, 9, 4, 6, 8'.split(', ')
    for i in range(10):
        cnt1 = int(coefs1[i]) * int(p['tin'][i])
    cnt2 = 0
    coefs2 = '3, 7, 2, 4, 10, 3, 5, 9, 4, 6, 8'.split(', ')
    for i in range(11):
        cnt2 = int(coefs2[i]) * int(p['tin'][i])
    cnt1 = str(cnt1 % 11)[-1]
    cnt2 = str(cnt2 % 11)[-1]
    if cnt1 != p['tin'][10] or cnt2 != p['tin'][11]:
        ans2 = -1
    return (ans1, ans2)