with open('numbers.txt') as infile:
    data = [int(i.rstrip()) for i in infile.readlines()]


ans_even = 0
ans_odd = 0

#Cnt odd and even sums

with open('result.txt', 'w') as out:
    print(ans_even, ans_odd, file=out)