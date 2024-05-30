# functions take arguments which are internally handled as tuple or dict

def fnA(*args): # the asterisk * lets us gather all positional arguments together
    '''this function will accept positional arguments x, y, z
    If we only have one argument, it will be converted into an integer
    If we have two arguments they will be added
    Three arguments will be multiplied together'''
    # what is the nature of the positional arguments
    # print(args, type(args)) # we have a tuple
    if len(args) == 1:
        return int(args[0])
    if len(args)==2:
        return args[0]+args[1]
    if len(args)==3:
        return args[0]*args[1]*args[2]
    return # in all other cases do nothing


if __name__ == '__main__':
    fnA(2.345) # one argument
    fnA(4,5)   # two arguments
    fnA(7,8,9) # three arguments
    fnA(4,3,2, True, fnA, 'clever', {}, [], ('A',)) # arbitrary values passed as positional arguments 