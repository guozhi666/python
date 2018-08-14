# -*- coding:utf-8 -*-
#判断类型 (isinstance)
class Person(object):

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

class Student(Person):

    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score

class Teacher(Person):

    def __init__(self, name, gender, course):
        super(Teacher, self).__init__(name, gender)
        self.course = course

t = Teacher('Alice', 'Female', 'English')

#判断 t 是否是 Person，Student，Teacher，object 类型，
print isinstance(t,Person)
print isinstance(t,Student)
print isinstance(t,Teacher)
print isinstance(t,object)