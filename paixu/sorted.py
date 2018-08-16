# -*-coding:utf-8 -*-

# enumerate 的调用
#用于将一个可遍历的数据对象组合成一个索引序列
lst= [2,8,6,4,5,7,9]

def sort (lst, fn=lambda a,b :a>b):
    newlist = []
    for x in lst:
        for i,y in enumerate(newlist):
            if fn(x,y):
                newlist.insert(i,x)
                break
        else:
            newlist.append(x)
    return newlist
print sort(lst)

print (list(map(lambda x: (x,x+1),lst)))