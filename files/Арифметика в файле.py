with open('in_file.txt') as infile, open('out_file.txt', 'w') as outfile:
    s = [i.rstrip() for i in infile.readlines()]
    ans = [eval(i) for i in s]
    for i in range(len(s)):
        print('{} =  {}'.format(s[i], ans[i]), file=outfile)


