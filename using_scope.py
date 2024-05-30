# remember we can declare code blocks using a colon
# def: for: if: class: all create a code block also known as a scope

# we try to avoid poluting the global scope
g = 'this is in the global scope (no particular code block)'

def local():
    '''this code block has its own scope'''
    global g # we now have access to the global g within this scope
    g = 'this is within the code block of a function'

if __name__ == '__main__':
    print(g)
    local() # this function will set a new value for g
    print(g)