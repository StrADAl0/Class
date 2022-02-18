def genome(line1, line2):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    cnt = 0
    for i in range(len(line1)):
        if line2[i] != complement[line1[i]]:
            continue
        cnt += 1
    return (cnt, (cnt / len(line1) >= 0.3))
