# -- coding: UTF-8 --

import math

def format_name(s):
    return s[0].upper() + s[1:].lower()
	#map()高阶函数
	#它接收一个函数 f 和一个 list，
	#并通过把函数 f 依次作用在 list 的每个元素上，
	#得到一个新的 list 并返回。
print map(format_name, ['adam', 'LISA', 'barT'])


def prod(x, y):
    return x*y
	#reudce()高阶函数
	#reduce()传入的函数 f 必须接收两个参数，reduce()对list的每个元素反复调用函数f，并返回最终结果值。
print reduce(prod, [2, 4, 5, 7, 12])


def is_sqr(x):
	#filter()高阶函数
	#filter()根据判断结果自动过滤掉不符合条件的元素，返回由符合条件元素组成的新list。
    r = int(math.sqrt(x))
    return r*r==x

print filter(is_sqr, range(1, 101))