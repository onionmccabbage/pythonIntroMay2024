
# here are some utility functions
def isOdd(n):
    '''return True if odd, False otherwise'''
    return n%2 !=0

def addThem(m,n):
    '''return hte sum of m and n'''
    return m+n

def main():
    '''make use of our utilities in higher order code'''
    r = range(-99,100) # from -99 to 99
    odds = map(isOdd, r) # apply the isOdd function to every member of the range
    print(odds) # we have a map object (iterable)
    for i in odds:
        print(i, end=', ')
    # we can use filter to apply a function and return only matching values
    v = (-7, -5, -4, 2, 5, 9, 11, 3)
    my_odds = filter(isOdd, v)
    print(my_odds) # a filter object
    for i in my_odds:
        print(i) # we only have the members of the collection which match the filter function
    # print(my_odds.__next__()) # -7
    # print(my_odds.__next__()) # -5
    # print(my_odds.__next__()) # 5

if __name__ == '__main__':
    main()