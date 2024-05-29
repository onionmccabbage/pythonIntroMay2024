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

def handleUserInput():
    '''ask the user to enter a value'''
    # remember - here we are I/O bound (wait for input or output)
    v = input('Please enter a number: ') # the code will pause until the user has entered something
    # be careful - EVERY user input will be a STRING
    # Typically we can convert the inout to a numeric value
    v_num = float(v)
    # we may choose to format a nice string (with \n for new line)
    r = f'The value {v_num} is {type(v_num)}.\nIs it odd? {isOdd(v_num)}' # the f says format this string
    return r

# what does Python call this module?
print(f'This module is called {__name__}')  # __main__ when run directly

if __name__ == '__main__': 
    # every time we execute a module directly, 
    # Python will name that module __main__
    # If a module gets imported elsewhere, Python will NOT call that module __main__
    '''we tend to use this kind of structure within every python module'''
    r = handleUserInput() # invoke our function
    print(r)
    r1 = addThem(3,4)
    r2 = addThem('5', '7')
    r3 = addThem('three', 'four')
    r4 = addThem(3.5, 7.2)
    print(r1, r2, r3, r4)
    print( isOdd(99) ) # True
    print( isOdd(88) ) # False




