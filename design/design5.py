# -*- coding:utf-8 -*-

#  __iter__
class Fib():
    def __init__(self):
        self.__a, self.__b = 0, 1
    def __iter__(self):
        return self
    def next(self):
        self.__a, self.__b = self.__b, self.__a + self.__b
        if self.__a > 1000:
            raise StopIteration
        else:
            return self.__a
for x in Fib():
    print(x)

print('-------------------\n')

class Su ():
    def __init__(self):
        self.name = 'CC'
    def __getattr__(self, item):
        if item == 'score':
            return '99'
print (Su().score)