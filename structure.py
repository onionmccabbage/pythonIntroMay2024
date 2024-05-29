# how to structure python modules
# using functions, loops, conditionals, __main__
# we may choose to provide default values for the arguments
def myFn(a=3, b=(9,8,7,6,5)): # the colon indicates the start of a code block
    # a = 3
    # b = (4,5,6,7,8)
    if type(b)==tuple:
        r = a/b[3]
    else:
        r = a/b
    # careful - code blocks end when their indentation ceases
    return r    # every indented line belongs to this code block
# when the lines are no longer indented, the code block has ended

# what does Python call this module?
print(__name__)

# single equals SETS equality, double equals CHECKS equality
if __name__ == '__main__': # by default the current module is called __main__
    '''This code will ONLY run when this module is run directly (not if it is imported elsewhere)'''
    c = (6,5,4,3,2)
    for i in c: # we can iterate over ANY indexed collection (string, tuple, list)
        r = i*i
        print(r)

    # we can override the defaults with our own values
    result = myFn(5, (4,5,6,7,8)) # we invoke the function
    result = myFn(5, 2) # we invoke the function (override defaults for a nad for b)
    # we can override either of the defaults (or neither)
    result = myFn(a=3) # takes the default for b
    result = myFn(b=3) # takes the default for a
    result = myFn(3) # takes the default for b
    result = myFn(3, b=9) # implicitly override a (its positionally the first argument)
    print(result)
