import json

def askUserCat():
    '''ask the user for a valid category'''
    while True:
        cat = input('Pick a category: ')
        if cat.lower() in ('users', 'todos', 'photos', 'posts'):
            break
    return cat

def loadJSON(f):
    '''load a JSON file'''
    filename = f'{f}.json'
    try:
        with open(filename, 'rt') as fin:
            j = fin.read() # read in the entire JSON text file
        return j
    except Exception as err:
        print(f'Problem: {err}')

def showData(d):
    '''iterate over the structure to show members'''
    for _ in d:
        print(_)

def showTodos(todos):
    '''Show the todos nicely formatted'''
    for todo in todos:
        print(f'{todo['id']}: {todo['title']} completed:{todo['completed']}')

def showUsers(users):
    '''show users nicely formatted'''
    for user in users:
        print(f'{user['name']} {user['email']}')

def showPhotos(photos):
    '''show photos nicely formatted'''
    for photo in photos:
        print(f'{photo['title']} {photo['thumbnailUrl']}')

def showPosts(posts):
    '''show posts nicely formatted'''
    for post in posts:
        print(f'{post['title']} {post['body']}')

def getId(cat):
    '''ask the user for a valid ID'''
    limits = {'users':10, 'posts':100, 'todos':200, 'photos':5000}
    while True:
        try:
            whichId =int(float(input(f'Which ID to store: ')))
        except:
            pass
        if whichId >0 and whichId < limits[cat]:
            break
    return whichId

def writeFile(c,i,s):
    '''write a single data member to a text file'''
    newFileName = f'{c}{i}.txt'
    j = json.dumps(s)
    with open(newFileName, 'wt') as fout: # overwrite if exists
        fout.write(j)

def main():
    whichCat = askUserCat()
    retrieved = loadJSON(whichCat)
    struct = json.loads(retrieved)
    if whichCat=='todos':
        showTodos(struct)
    elif whichCat == 'users':
        showUsers(struct)
    elif whichCat == 'photos':
        showPhotos(struct)
    elif whichCat == 'posts':
        showPosts(struct)
    else:
        showData(struct)
    whichId = getId(whichCat)
    writeFile(whichCat, whichId, struct)

if __name__ == '__main__':
    main()