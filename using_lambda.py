# a lambda function is useful when we dont need all the bother of defining a normal function

def fn(x,y):
    '''return x to the power of y'''
    return x**y

def flip(f): # we expect a function incoming
    '''flip the positional arguments of another function'''
    return lambda x,y:f(y,x) # a non-persistent function

if __name__ == '__main__':
    r = fn(25, 0.5) # 5.0
    print(r)
    s = flip(fn)
    print(s(25, 0.5)) # this calls fn(0.5, 25)
