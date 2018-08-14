# -*- coding:utf-8 -*-
#多重继承
# 通过多重继承，请定义“会打篮球的学生”和“会踢足球的老师”。
class Person(object):
    pass

class Student(Person):
    pass

class Teacher(Person):
    pass

class SkillMixin(object):
    pass

class BasketballMixin(SkillMixin):
    def skill(self):
        return 'basketball'

class FootballMixin(SkillMixin):
    def skill(self):
        return 'football'

class BStudent(Student, BasketballMixin): #多重继承，继承学生和篮球
    pass

class FTeacher(Teacher, FootballMixin): #多重继承， 继承教师和足球
    pass

s = BStudent()
print s.skill()

t = FTeacher()
print t.skill()