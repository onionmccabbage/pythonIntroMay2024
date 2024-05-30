def readTextFile(fn):
    '''read back from a text file and return the result'''
    try:
        fin = open(fn, 'rt') # fin for file input 'rt' will read text
        retrieved = fin.read() # read the entire file
        # retrieved = fin.readlines() # read the entire file into a list of lines
        # retrieved = fin.readline() # read one line, or n characters
        fin.close()
        return retrieved
    except Exception as err:
        print(f'Problem:{err}')

def elegantReader(fn):
    ''' read an entire file using with'''
    try:
        with open(fn, 'rt') as fin:
            r = fin.read()
    except Exception as err:
        print(f'Problem:{err}')
    finally:
        return r

if __name__ == '__main__':
    r = readTextFile('my_log.txt')
    print(r)
    s = elegantReader('my_log.txt')
    print(s)