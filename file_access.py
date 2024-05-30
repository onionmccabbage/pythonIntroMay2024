# here we will write and read text files. Maybe Byte files (if time)
def printToFile(s):
    '''commit the string s to a file'''
    # we need a file access object
    # 'wt' will (over)write text 'xt' for exlusive access
    try:
        fout = open('my_log.txt', 'at') # 'at' lets us append text
        print(s, file=fout) # write to our file acces object (print defaults to new-line at the end)
        fout.close() # we should tidy up at the earliest opportunity
    except FileExistsError as fe:
        print(f'Problem: the file already exists')

def writeToFile(s):
    '''commit the string to a file using file writing'''
    try:
        fout = open('my_log.txt', 'at')
        fout.write(s) # write or writelines
        fout.close()
    except Exception as err:
        print(f'There was a problem: {err}')

if __name__ == '__main__':
    # printToFile('this text will be commited to a file')
    writeToFile('this text \nwill be written \nto a file') # \n is a new line