import random # this is a library provided by python

# here we meet the range object - reeally useful for iterating, checking, etc.
def myRange():
    # ranges are brillian because their values NEVER exist in memory all at once
    r = range(-99, 99, 2) # start, stop-before, step
    return r

def checkPrime(n):
    '''Check if n is a prime number'''
    primes_t = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97)
    if n in primes_t:
        return True
    return False # we could use else here

if __name__ == '__main__':
    result = myRange()
    print(result, type(result))
    # we may use a range to iterate
    for _ in result:
        print(_) # _ is often used as a meaningless iterable
    # check for prime numbers
    l = [] # empty list
    for _ in range(0, 101): # start at , stop before 101 (default step 1)
        l.append( checkPrime(_) )
    print(l)
    # make use of the random library
    rand = random.randint(0,100) # give me a random integer between 0 and 100 inclusive
    print(f'The value {rand} is prime? {checkPrime(rand)}')