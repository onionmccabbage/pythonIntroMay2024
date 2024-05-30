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

def fnB(**kwargs): # **kwargs will gather all keyword arguments into a dict
    '''all the keyword arguments will be gathered into a dict'''
    r = ''
    for (k,v) in kwargs.items():
        r = r+f'Key {k} contains {v}\n'
    return r

# all positional argumetns MUST come before any keyword arguments
def fnC(*args, **kwargs):
    '''any arguments will be in a tuple, any kwargs will be in a dict'''
    return (args, kwargs)


if __name__ == '__main__':
    print( fnA(2.345) ) # one argument
    print( fnA(4,5) )   # two arguments
    print( fnA(7,8,9) ) # three arguments
    fnA(4,3,2, True, fnA, 'clever', {}, [], ('A',)) # arbitrary values passed as positional arguments 
    print( fnB(x=3, n='Floela', e='nonsuch@dooby.ie', fn=fnB, l=[5,4,3,2,1]) )
    print( fnC(4,3,2, True, fnA, 'clever', {}, [], ('A',), x=3, n='Floela', e='nonsuch@dooby.ie', fn=fnB, l=[5,4,3,2,1]) )