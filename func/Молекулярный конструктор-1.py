complement = {'G': 'C', 'A': 'T', 'T': 'A', 'C': 'G'}


def molecule_assembly(data=[], dna2='', overwrite=False):
    ans = []
    for i in molecule_dna:
        t = i[0] + i[1]
        ans.append(t)
    global dna_chain
    if overwrite:
        dna_chain = dna2
    else:
        dna_chain = dna_chain + dna2
    dna1 = []
    for i in data:
        for j in i:
            dna1.append(j)
    while True:
        if len(dna_chain) == 0: 
            break
        if complement[dna_chain[0]] in dna1:
            t = dna_chain[0], dna1[dna1.index(complement[dna_chain[0]])]
            molecule_dna.append(t)
            ans.append(dna_chain[0] + dna1[dna1.index(complement[dna_chain[0]])])
            dna1.pop(dna1.index(complement[dna_chain[0]]))
            dna_chain = dna_chain[1:]
        else:
            break
    return ans
