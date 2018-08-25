# -*- coding:utf-8 -*-

a = '字符串拼接1'
b = '字符串拼接2'

c = a + b
d = "%s%s"%(a, b)
e = "{a}{b}" .format(a = a, b = b)
f = "".join([a, b])

print (c)
print (d)
print (e)
print (f)

