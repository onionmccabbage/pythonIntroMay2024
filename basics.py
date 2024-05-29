# comments look like this

# we can write immediate code here
a = 3   # an integer
b = 7.2 # a floating point value
c = False # or True boolean type
n = None  # comes in handy
print(b/a)
print( type(a), type(b) )

# there is a string data type. a string is an immutable indexed collection of characters
s = '''here is a 
string 
of              charac
ters'''
# wemay use single quotes, double quotes or triple quotes for strings
# triple quotes let us preserve witespace in a string
# strings let us use slicing
print( s[2:17:2] ) # [start:stop-before:step]
print(s, type(s))

# other collection types: tuple and a list
# a tuple is an immutable indexed collection of any data type

t = (4,3,2,'hello', False, s, None, 77)

print(t[3:5]) # hello, False

# a list is a mutable indexed collection of any data type
l = [3,'coffee', 'coffee', 9, True, t]
print(l, type(l), l[2:4])
l.append('added')
l.append(a)
l[4] = 'changed'
l.pop() # remove the top-most member (the highest index member)
l.pop(3) # remove the specific index member
l.remove('coffee') # remove member this member
print(l)

# for efficiency, use a tuple when you do not need to mutate, use a list when you do

# dictionary: a non-indexed collection of any data type as key:value pairs
d = {'fn':'Floela', 'ln':'Benjamin', 'age':46, 'status':'admin', t:99, True:None}
# NB we usually stick to strings for the keys
print(type(d), d, d['age'], d['fn'])
# a set is a non-indexed mutable collection of any data type unique members
my_set = {7,6,5,'tea', False, 7, 'tea'}
my_set.add(7)
my_set.add(8)
my_set.add('more')

print(my_set, type(my_set))

# what does Python call this module?
print(__name__)