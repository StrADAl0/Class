immunoglobulins = []
def vaccine_effect(value):
    for i in range(len(immunoglobulins)):
        if immunoglobulins[i][1] < 1:
             immunoglobulins.pop(i)