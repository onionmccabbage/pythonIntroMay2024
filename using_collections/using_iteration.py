# here we will build tuple, list and dict object then iterate over members

l = []
k = list(('Ethel', 'Deidre', 'Enit', 'Fran')) # we put a tuple into our list
for i in k:
    print(i)

m = (4,) # a one-member tuple - careful dont just write (4)
n = (4, 6, 20) # here we have a tuple
for i in n:
    print(i)
t = tuple() # an empty tuple - very pointless!!

d = dict() # explicit dict
e = {'n':k[0], 'age':n[2], 'recent':True, 'gender':'cis'}
# we can iterate over a dict
for (k,v) in e.items(): # by convention (k,v) for key,value. Careful items() is a method
    print(f'key {k} has value {v}')

s = set()