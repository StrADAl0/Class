import json
import csv

with open('taxpayer_in.json', encoding='utf8') as infile1:
    payers = json.load(infile1)
with open('regions.csv', encoding='utf8') as infile2:
    regions = list(csv.DictReader(infile2, delimiter=';'))

coefs1 = '7, 2, 4, 10, 3, 5, 9, 4, 6, 8'.split(', ')
coefs2 = '3, 7, 2, 4, 10, 3, 5, 9, 4, 6, 8'.split(', ')


def check_client(name):
    lastname, firstname, middlename = name
    result, tin = False, None
    for i in payers:
        if i['lastname'] == lastname and \
            i['firstname'] == firstname and \
                i['middlename'] == middlename:
                result, tin = True, i['tin']
                break
    return (result, tin)


def check_region(tin, place):
    code = None
    for i in regions:
        if i['region_name'] == place:
            code = i['region_code']
            break
    if code is None:
        return -1
    if tin[:2] != str(code):
        return -1
    return 0


def check_sums(tin):
    ans = 0
    sum1, sum2 = 0, 0
    for i in range(10):
        sum1 += int(tin[i]) * int(coefs1[i])
        sum2 += int(tin[i]) * int(coefs2[i])
    sum2 += int(tin[10]) * int(coefs2[10])
    if str(sum1 % 11)[-1] != tin[10]:
        ans = -1
    if str(sum2 % 11)[-1] != tin[11]:
        ans = -1
    return ans


def check_security(name, place):
    tin = check_client(name)[1]
    if tin is None:
        return (None, None)
    ans1 = check_region(tin, place)
    ans2 = check_sums(tin)
    return (ans1, ans2)
