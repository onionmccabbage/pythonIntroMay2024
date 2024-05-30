# comprehension means dealing comprehenively with every member of a collection
from using_iteration import n as my_tuple, k as my_list, e as my_dict

def findCaracterFreq(s):
    '''count the frequency of every character in a string'''
    char_d = {letter:s.count(letter) for letter in s}
    return char_d

if __name__ == '__main__':
    t = [n for n in my_tuple] # tuple comprehension
    s = [n for n in my_list]  # list comprehension
    r = [n*n for n in range(0,11)] # range comrehension
    print(r, type(r))
    print( findCaracterFreq('how many of each letter do we have?') )

