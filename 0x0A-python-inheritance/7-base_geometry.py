#!/user/bin/python3
'''
Module 7-base_geometry
Classes
    BaseGeometry
'''


# SuperClass
class BaseGeometry():
    '''Empty BaseGeometry class object'''
    pass

# Area | public method un-implemented
    def area(self):
        '''raises an exception'''
        raise Exception("area() is not implemented")

# Integer validator | public method
    def integer_validator(self, name, value):
        '''validate if 'value' is an integer
        Arguments
            name: string with the name of object
            value: object to validate
        '''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
