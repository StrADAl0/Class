def func(*args, **kwargs):
    if('parity' in kwargs.keys()):
        if(kwargs['parity'] == 0):
            for i in range(len(args)):
                if(args[i] % 2 == 1):
                    args.pop(i)
        else:
            for i in range(len(args)):
                if(args[i] % 2 == 0):
                    args.pop(i)
    if('lower' in kwargs.keys()):
        for i in range(len(args)):
            if(args[i] >= kwargs['lower']):
                args.pop(i)
    if('to_sort' in kwargs.keys()):
        args = sorted(args, reverse = kwargs['to_sort'])
    return args
    