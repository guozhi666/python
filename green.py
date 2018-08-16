#-*-coding:utf-8-*-
def addx(x):
	def adder(y):
		return x + y
	return adder
	
#c = addx(8)

#print(type(c))
#-> <type 'function'>
#print(c.__name__)
#-> adder 
print(addx(8)(10))
#-> 18
print ("\n")
print ("\n<------------------>\n")
print ("\n")

def foo():
	m = 0
	def foo1():
		m = 1
		print m
		
	print m 
	foo1()
	print m 
	
foo()

print ("\n")
print ("\n<------------------>\n")
print ("\n")

print ("学号\t姓名\t语文\t数学\t英语")
print ("01\t发放\t38\t68\t56")
print ("01\t发放\t38\t68\t56")
print ("01\t发放\t38\t68\t56")
print ("01\t发放\t38\t68\t56")

print ("\n")
print ("\n<------------------>\n")
print ("\n")

def foo():
	a = [1]
	def bar():
		a[0] = a[0] + 1
		return a[0]
	return bar

c = foo()
print c()

print ("\n")
print ("\n<------------------>\n")
print ("\n")



for i in range(3):
	def foo(x, y = i):
		print x + y
		flist.append(foo)
		return flist


print ("\n")
print ("\n<------------------>\n")
print ("\n")

		
origin = [0, 0] #系统坐标原点
legal_x = [0, 50]#x轴合法坐标
legal_y = [0, 50]#y轴合法坐标
def create(pos = origin):
	def player(direction,step):
		new_x = pos[0] + direction[0]*step
		new_y = pos[1] + direction[1]*step
		pos[0] = new_x
		pos[1] = new_y
		#此处不能写成 pos = [new_x,new_y],原因是闭包的局部变量
		return pos 
	return player
player = create()    #创建棋子player，起点为原点
print player([1,0],10)#向X轴正方向移动10步
print player([0,1],20)#向Y轴正方向移动20步
print player([-1,0],10)#向X轴负方向移动10步