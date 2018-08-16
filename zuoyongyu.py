# -*-coding:utf-8 -*-

Money = 100
def AddMoney():
    global Money  #  global  强制声明此处Money为局部变量，避免与全局变量Money冲突
    Money = Money + 1

print Money
AddMoney()
print Money