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
        self.__x = x # we use __x to 'mangle' the access to x
        self.__y = y # mangling prevents direct acces to the values
    # to provide access to these mangled properties, we write 'getter' and 'setter' methods
    # also known as accessor and mutator methods
    @property # this is a decorator (note the @ sign)
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y

if __name__ == '__main__':
    p1 = Point2d(3,4) # we now have an instance of our class (calls the __init__ method)
    p2 = Point2d(-3,-4) # we now have an instance of our class (calls the __init__ method)
    p3 = Point2d(4,3) # we now have an instance of our class (calls the __init__ method)
    print(p1.x, p1.y) # this invokes the property function x and y