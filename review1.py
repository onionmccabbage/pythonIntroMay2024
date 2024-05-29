# Python review exercise: guess the random number between 0-100
from random import randint # we need a way to make random numbers

def game():
    ''' ask user to guess a random integer 0-100 '''
    target = randint(0,100) # up to 100 inclusive
    # create collections of odds, evens, squares and primes
    odd_ints     = range(1,100, 2) 
    even_ints    = range(0, 101, 2)
    squares_list = []
    for i in range(0, 11):
        squares_list.append(i*i)
    primes_t = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97)
    # set some boolean flags regarding the nature of our target number
    is_odd    = target in odd_ints
    is_even   = target in even_ints
    is_square = target in squares_list
    is_prime  = target in primes_t
    guess = 999 # set an initial value that is out of range
    # keep the game running
    # for guess_counter in range(999): # keep going for 999 guesses!!
    while True: # careful - this will run forever!!!!!
        guess = int(float(input('guess:'))) # make sure it's an int
        # if guess != target:
            # conditionally act on the guess
        if guess == -2: # do they want a clue
            print (f'CLUE: odd: {is_odd} even: {is_even} square: {is_square} prime: {is_prime}' )
        elif guess == -1: # do they want to quit
            print (f'it was {target}' )
            guess = target # break # stops the current loop
            # return # break out of the function
            break # this will end the while loop
        elif guess > target: # is the guess too high
            print('too high')
        elif guess < target: # is the guess too low (could be an else clause)
                print('too low')
        else:
            print(f'correct it was {target} ') # you took {guess_counter} tries' )
            # return
            quit # quit out of the loop

if __name__ == '__main__':
    game()
