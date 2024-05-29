from class_a import Point2d # we will extend our class

class Point3d(Point2d): # by default every class inherits from object
    '''this class takes everything from our 2-d point and lets us extend it
    we will add a numeric value for z'''
    __slots__ = ['__x', '__y', '__z']
    def __init__(self, x, y, z):
        ''' we call the initializer of the parent class'''
        Point2d.__init__(self, x, y) # all the features of x and y will be handled
        self.z = z
    @property
    def z(self):
        return self.__z # remember to use name mangling
    @z.setter
    def z(self, new_z):
        if type(new_z) in (int, float):
            self.__z = new_z
        else:
            raise TypeError
    def __str__(self): # EVERY object in Python has a __str__ method
        '''we override the __str__ method to choose how we would like this to print'''
        # NOTE we invoke hte GETTER for x, y and z we do not access them directly
        return f'this is a Point in 3-d space x:{self.x} y:{self.y} z:{self.z}'

if __name__ == '__main__':
    pA = Point3d(3,4,5)
    pB = Point3d('3',2,1) # will use the default for x

    print(pB)