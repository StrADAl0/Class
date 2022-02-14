import csv
def messier_search(param):
    ans = []
    with open('messier.csv', encoding='utf-8') as infile:
        data = list(csv.DictReader(infile, delimiter=';'))
    for i in data:
        ans.append(i[param])
    return sorted(ans)