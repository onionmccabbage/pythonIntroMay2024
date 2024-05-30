# here we will build tuple, list and dict object then iterate over members
k = list(('Ethel', 'Deidre', 'Enit', 'Fran')) # we put a tuple into our list
n = (4, 6, 20) # here we have a tuple
e = {'n':k[0], 'age':n[2], 'recent':True, 'gender':'cis'}

if __name__ == '__main__':
    l = []
    for i in k:
        print(i)

    m = (4,) # a one-member tuple - careful dont just write (4)
    for i in n:
        print(i)
    t = tuple() # an empty tuple - very pointless!!

    d = dict() # explicit dict
    # we can iterate over a dict
    for (k,v) in e.items(): # by convention (k,v) for key,value. Careful items() is a method
        print(f'key {k} has value {v}')
    for k in e.keys():
        print(k, e[k])
    for v in e.values():
        print(v)

    # we can work strings
    s = 'strings are collections of UTF characters'
    print(len(s))
    for i in s:
        print(i, end=', ') # by default print always ends with a new line but we can specify our own termination character

    s = set()