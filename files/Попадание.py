from sys import stdin


nums = [int(i.rstrip()) for i in stdin]


ans = []
for i in range(len(nums)):
    if(nums[i] == i + 1):
        ans.append(i + 1)


with open('output.txt', 'w') as out:
    if(not ans):
        print(0, file=out)
    else:
        print(*ans, file=out)
