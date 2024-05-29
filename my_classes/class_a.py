# we can declare as many classes as we like in Python

# here is a demo
myPoint_1 = {'x':3, 'y':4} # here we have x and y
myPoint_2 = (4,3)
myPoint_3 = [4,3]
# none of the above let me validate the values of x and y
myPoint_1['x'] = 'wibble'
myPoint_3[0] = True

class Point2d(): # the brackets are optional
    '''Here we encapsulate a geometric point in 2-d space
    x and y will be floating point values (no defaults)'''
    def __init__(self, x, y): # every class method MUST take 'self' as an argument
        '''this is the initialiser for the class. 
        It is run every time we make a new instance'''
        # print(self)
        self.x = x # we call the setter for x (and use mangling)
        self.y = y # mangling prevents direct acces to the values
    # to provide access to these mangled properties, we write 'getter' and 'setter' methods
    # also known as accessor and mutator methods
    @property # this is a decorator (note the @ sign)
    def x(self):
        return self.__x # we may do anything but here we just return the mangled value
    @x.setter # this decorator is the 'setter' or 'mutator' method for x
    def x(self, new_x):
        '''we can validate the incoming value before setting'''
        if type(new_x) in (int, float):
            self.__x = new_x
        else:
            self.__x = 0 # we may choose to set a default
    @property # this is the getter or the accessor for the property
    def y(self):
        return self.__y
    @y.setter
    def y(self, new_y):
        '''validate y is eiher int or float'''
        if type(new_y) in (int, float):
            self.__y = new_y
        else:
            raise TypeError # we may choose ot raise an exception

if __name__ == '__main__':
    p1 = Point2d(3,4) # we now have an instance of our class (calls the __init__ method)
    p2 = Point2d(-3.00,-4.00) # float values pass valiation
    p3 = Point2d('4',3) # x will takethe default of zero
    try: # wrap dodgy code in a try-except block
        p4 = Point2d('4','3') # y fails validation and raises a type error
    except TypeError as te:
        print(f'Something went wrong: {te}')
    except Exception as err: # we can handle any and every expected exception
        print(err)
    finally: # this always runs, whether or not we have an exception
        pass
    print(p1.x, p1.y) # this invokes the property function x and y