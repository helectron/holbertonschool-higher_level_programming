'''
module 9-student
Class:
    Student 
'''


class Student:
    '''Creates an intance of Student '''
    def __init__(self, first_name, last_name, age):
        '''Constructor for students'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns dict representation of student instance"""
        return self.__dict__