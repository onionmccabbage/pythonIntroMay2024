from class_a import Point2d # we will extend our class

class Point3d(Point2d): # by default every class inherits from object
    '''this class takes everything from our 2-d point and lets us extend it
    we will add a numeric value for z'''
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

if __name__ == '__main__':
    pA = Point3d(3,4,5)
    pB = Point3d('3',2,1) # will use the default for x

    print(pB) # <__main__.Point3d object ....>