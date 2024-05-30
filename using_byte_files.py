def makeBytes(s):
    '''convert a string into bytes'''
    b = s.encode() # encode will convert any string into bytes
    return b # remember to return the bytes

def makeText(b):
    '''convert bytes to text'''
    t = b.decode()
    return t

def writeBytes(b):
    '''commit bytes to a file'''
    try:
        with open('my_bytes', 'ab') as fout: # 'ab' will append bytes
            fout.write(b)
    except Exception as err:
        print(f'problem {err}')

def readBytes():
    try:
        with open('my_bytes', 'rb') as fin:
            r = fin.read()
    except Exception as err:
        print(f'problem {err}')
    finally:
        return r

if __name__ == '__main__':
    b = makeBytes('here is plain text\n')
    writeBytes(b)
    r = readBytes()
    t = makeText(r)
    print(t)
    