# comprehension means dealing comprehenively with every member of a collection
from using_iteration import n as my_tuple, k as my_list, e as my_dict

if __name__ == '__main__':
    t = [n for n in my_tuple] # comprehension
    print(t, type(t))

