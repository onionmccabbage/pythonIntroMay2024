# here we examine iterable collections, the range object and user input
# also basic conditionals for validation
def addThem(a,b): # NB here we elect to NOT provide default values
    '''here we check that a and b are numeric then add their values'''
    # if (type(a)== int or type(a)==float) and (type(b)==int or type(b)==float):
    if type(a) in (int, float) and type(b)in (int, float):
        result = a+b
    # isnumeric can check if a stting contains only digits
    elif a.isnumeric() and b.isnumeric(): # isnumeric checks it contains ONLY digits
        a = int(a)
        b = int(b)
        result = a+b
    else:
        result = 'Sorry, cannot add non numeric values'

    return result

def isOdd(n):
    '''return True if n is odd, False otherwise'''
    if n/2 != n//2: # the // is modulo division (% gives the remainder)
        result = True
    else:
        result = False
    return result

# what does Python call this module?
print(__name__) # __main__ when run directly

if __name__ == '__main__': 
    # every time we execute a module directly, 
    # Python will name that module __main__
    # If a module gets imported elsewhere, Python will NOT call that module __main__
    '''we tend to use this kind of structure within every pythno module'''
    r1 = addThem(3,4)
    r2 = addThem('5', '7')
    r3 = addThem('three', 'four')
    r4 = addThem(3.5, 7.2)
    print(r1, r2, r3, r4)
    print( isOdd(99) ) # True
    print( isOdd(88) ) # False




