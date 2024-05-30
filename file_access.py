# here we will write and read text files. Maybe Byte files (if time)
def printToFile(s):
    '''commit the string s to a file'''
    # we need a file access object
    # 'wt' will (over)write text 'xt' for exlusive access
    try:
        fout = open('my_log.txt', 'xt') # 'at' lets us append text
        print(s, file=fout) # white to our file acces object
    except FileExistsError as fe:
        print(f'Problem: the file already exists')

if __name__ == '__main__':
    printToFile('this text will be commited to a file')