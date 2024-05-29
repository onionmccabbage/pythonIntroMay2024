# here we examine iterable collections, the range object and user input
# also basic conditionals for validation
def addThem(a,b): # NB here we elect to NOT provide default values
    '''here we check that a and b are numeric then add their values'''
    if type(a)== int and type(b)==int:
        result = a+b
    elif a.isnumeric() and b.isnumeric(): # isnumeric checks it contains ONLY digits
        a = int(a)
        b = int(b)
        result = a+b

    return result

if __name__ == '__main__':
    '''we tend to use this kind of structure within every pythno module'''
    r1 = addThem(3,4)
    r2 = addThem('5', '7')
    print(r1, r2)




