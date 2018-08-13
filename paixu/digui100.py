# -- coding:utf-8 --

def las( num):

    if num == 1:
        return 1
    return num + las(num-1)
print las(100)